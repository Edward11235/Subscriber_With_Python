import datetime
import cv2
import numpy as np
import struct
import json
from subscriber import PacketDeserializer

packet_deserializer = PacketDeserializer(5001)
packet_deserializer.start()

while True:
    packet = packet_deserializer.read()
    if packet['type'] == 1:  # If the packet is an image
        # size = struct.unpack('!I', packet['payload'][:4])[0]  # get the size of the image data
        array = np.frombuffer(packet['payload'][8:], dtype=np.uint8)  # get the image data
        img = cv2.imdecode(array, cv2.IMREAD_COLOR)

        with open('rawdata.jpg', 'wb') as f:
            f.write(packet['payload'][8:])

        # flags = [cv2.IMREAD_COLOR, cv2.IMREAD_GRAYSCALE, cv2.IMREAD_UNCHANGED, cv2.IMREAD_REDUCED_GRAYSCALE_2, 
        #     cv2.IMREAD_REDUCED_COLOR_2, cv2.IMREAD_REDUCED_GRAYSCALE_4, cv2.IMREAD_REDUCED_COLOR_4,
        #     cv2.IMREAD_REDUCED_GRAYSCALE_8, cv2.IMREAD_REDUCED_COLOR_8, cv2.IMREAD_IGNORE_ORIENTATION]

        # for flag in flags:
        #     img = cv2.imdecode(array, flag)
        #     if img is not None:
        #         if img.size != 0:
        #             timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        #             cv2.imwrite(f'image_{timestamp}_{flag}.jpg', img)
        #         else:
        #             print(f"Decoded image is empty with flag {flag}.")
        #     else:
        #         print(f"Failed to decode image with flag {flag}.")

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






# //send image
# std::vector<uchar> data;
# cv::imencode(".jpg", color_image, data);
# unsigned char * array = new unsigned char[data.size()];
# std::memcpy(array, data.data(), data.size());
# channel.write(1, array, data.size());
# delete[] array;