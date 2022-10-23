#!/usr/bin/env python3
# SPDX-License-Identifier: 0BSD

# Copyright (C) 2018 by Forest Crossman <cyrozap@gmail.com>
#
# Permission to use, copy, modify, and/or distribute this software for
# any purpose with or without fee is hereby granted.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL
# WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE
# AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL
# DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR
# PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
# TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.


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
