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
import sys
from datetime import datetime

try:
    import ath6kl_firmware
except ModuleNotFoundError:
    sys.stderr.write("Error: Failed to import \"ath6kl_firmware.py\". Please run \"make\" in this directory to generate that file, then try running this script again.\n")
    sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("firmware", type=str, help="The firmware binary you want to extract from.")
    args = parser.parse_args()

    split = args.firmware.split('.')
    ext = split[-1]
    basename = '.'.join(split[:-1])

    fw = ath6kl_firmware.Ath6klFirmware.from_file(args.firmware)
    for ie in fw.ies:
        if ie.id == ath6kl_firmware.Ath6klFirmware.IeTypes.fw_version:
            print("Firmware Version: {}".format(ie.data.version))
        elif ie.id == ath6kl_firmware.Ath6klFirmware.IeTypes.timestamp:
            ts = datetime.utcfromtimestamp(ie.data.timestamp)
            print("Timestamp: {}".format(ts.isoformat()))
        elif ie.id == ath6kl_firmware.Ath6klFirmware.IeTypes.fw_image:
            out_name = "{}.fw_image.{}".format(basename, ext)
            out = open(out_name, 'wb')
            out.write(ie.data)
            out.close()
            print("Wrote firmware image to \"{}\".".format(out_name))
        elif ie.id == ath6kl_firmware.Ath6klFirmware.IeTypes.capabilities:
            caps = struct.unpack('<I', ie.data)[0]
            print("Capabilities: 0x{:x}".format(caps))
        else:
            print("Unhandled id: {}".format(ie.id))
