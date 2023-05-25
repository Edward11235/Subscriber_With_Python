import cv2
import numpy as np
import struct
import json
from subscriber import PacketDeserializer
import datetime

# Create a PacketDeserializer instance listening on port 5001
deserializer = PacketDeserializer(5001)
deserializer.start()

while True:
    # Read the image packet, decode it, and save the image
    packet = deserializer.read()
    # if image_packet['type'] != 1:
    #     print("Warning: wrong type. Should be one")
    # array = np.frombuffer(image_packet['payload'], dtype=np.uint8)
    # img = cv2.imdecode(array, cv2.IMREAD_COLOR)
    # timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    # cv2.imwrite(f'image_{timestamp}.jpg', img)
    if packet['type'] == 1:  # If the packet is an image
        array = np.frombuffer(packet['payload'], dtype=np.uint8)
        img = cv2.imdecode(array, cv2.IMREAD_GRAYSCALE)  # Change to IMREAD_GRAYSCALE
        if img is None:
            print("Failed to decode image.")
        elif img.size == 0:
            print("Decoded image is empty.")
        else:
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            cv2.imwrite(f'image_{timestamp}.jpg', img)

    # Read the double number packet and print it
    value_packet = deserializer.read()
    value = struct.unpack('d', value_packet['payload'])[0]
    print("Received value: ", value)

    # Read the JSON packet, decode it, and print it
    json_packet = deserializer.read()
    json_str = json_packet['payload'].decode()
    json_parsed = json.loads(json_str)
    print("Received JSON: ", json_parsed)
