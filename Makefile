all: ath6kl_firmware.py

%.py: %.ksy
	kaitai-struct-compiler -t python $<
