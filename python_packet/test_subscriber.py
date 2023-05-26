import datetime
import cv2
import numpy as np
import struct
import json
from subscriber import PacketDeserializer

def compute_hash(payload):
    hash_value = 0
    for byte in payload:
        hash_value = hash_value * 31 + hash(byte)
    return hash_value

packet_deserializer = PacketDeserializer(5001)
packet_deserializer.start()
while True:
    packet = packet_deserializer.read()
    # if packet['type'] == 4:  # If the packet is a JSON
        # str_received = packet['payload'].decode()
        # with open('received_text.txt', 'w') as f:
        #     # Write the string into the file
        #     f.write(str_received)
        # # print(f"Received string: {str_received}")
        # print(len(str_received))

    # Compute the hash
    hash_value = compute_hash(packet['payload'])
    print("The hash of the payload is: ", hex(hash_value))
