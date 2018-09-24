#!/usr/bin/env python3

import argparse
import struct
from datetime import datetime


def gen_fw(fw_image):
    h = b'QCA-ATH6KL\0'

    fw_version = "3.5.0.999-1".encode('utf-8')
    h += struct.pack('<I', 0)
    h += struct.pack('<I', len(fw_version))
    h += fw_version

    timestamp = int(datetime.utcnow().timestamp())
    h += struct.pack('<I', 1)
    h += struct.pack('<I', 4)
    h += struct.pack('<I', timestamp)

    h += struct.pack('<I', 3)
    h += struct.pack('<I', len(fw_image))
    h += fw_image

    capabilities = 0x00074000
    h += struct.pack('<I', 6)
    h += struct.pack('<I', 4)
    h += struct.pack('<I', capabilities)
    return h

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str, help="Input file.")
    parser.add_argument("-o", "--output", type=str, default="fw-5.bin", help="Output file.")
    args = parser.parse_args()

    image = open(args.input, 'rb').read()
    binary = open(args.output, 'wb')
    binary.write(gen_fw(image))
    binary.close()
