import datetime
import cv2
import numpy as np
import struct
import json
from subscriber import PacketDeserializer

packet_deserializer = PacketDeserializer(5001)
packet_deserializer.start()

def crc32(data: bytes) -> int:
    polynomial = 0xEDB88320
    crc = 0xFFFFFFFF

    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ polynomial
            else:
                crc >>= 1

    return crc ^ 0xFFFFFFFF

while True:
    packet = packet_deserializer.read()
    if packet['type'] == 1:  # If the packet is an image
        # Compute the CRC32
        crc32_value = crc32(packet['payload'])
        print("The CRC32 of the payload is: ", hex(crc32_value))

        size = struct.unpack('!I', packet['payload'][:4])[0]  # get the size of the image data
        array = np.frombuffer(packet['payload'][4:size+4], dtype=np.uint8)  # get the image data
        img = cv2.imdecode(array, cv2.IMREAD_GRAYSCALE)
        if img is None:
            print("Failed to decode image.")
        elif img.size == 0:
            print("Decoded image is empty.")
        else:
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            cv2.imwrite(f'image_{timestamp}.jpg', img)
    elif packet['type'] == 2:  # If the packet is a double
        value = struct.unpack('!d', packet['payload'])[0]
        print(f"Received value: {value}")
    elif packet['type'] == 3:  # If the packet is a JSON
        json_str = packet['payload'].decode()
        json_parsed = json.loads(json_str)
        print(f"Received json: {json_parsed}")
