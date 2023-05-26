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

import datetime
import cv2
import numpy as np
import struct
import json
from subscriber import PacketDeserializer

def compute_hash(payload):
    return crc32(payload)

packet_deserializer = PacketDeserializer(5001)
packet_deserializer.start()
while True:
    packet = packet_deserializer.read()
    # Compute the CRC32
    crc32_value = compute_hash(packet['payload'])
    print("The CRC32 of the payload is: ", hex(crc32_value))
