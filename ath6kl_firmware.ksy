meta:
  id: ath6kl_firmware
  endian: le
  title: Firmware for ath6kl devices
  license: CC0-1.0
seq:
  - id: magic
    contents: "QCA-ATH6KL\0" # Magic includes the null byte.
  - id: ies
    type: ie
    repeat: eos
types:
  ie:
    seq:
      - id: id
        type: u4
        enum: ie_types
      - id: len
        type: u4
      - id: data
        size: len
        type:
          switch-on: id
          cases:
            'ie_types::fw_version': fw_version
            'ie_types::timestamp': timestamp
            # 'ie_types::otp_image': otp_image
            # 'ie_types::fw_image': fw_image
            # 'ie_types::patch_image': patch_image
            # 'ie_types::reserved_ram_size': reserved_ram_size
            # 'ie_types::capabilities': capabilities
            # 'ie_types::patch_addr': patch_addr
            # 'ie_types::board_addr': board_addr
            # 'ie_types::vif_max': vif_max
  fw_version:
    seq:
      - id: version
        type: str
        encoding: ASCII
        size-eos: true
  timestamp:
    seq:
      - id: timestamp
        type: u4
enums:
  ie_types:
    0: fw_version
    1: timestamp
    2: otp_image
    3: fw_image
    4: patch_image
    5: reserved_ram_size
    6: capabilities
    7: patch_addr
    8: board_addr
    9: vif_max
