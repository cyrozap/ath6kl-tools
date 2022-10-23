# ath6kl-tools


## Quick start

### Software dependencies

* Python 3
* [Kaitai Struct Compiler][ksc]
* [Kaitai Struct Python Runtime][kspr]

### Procedure

1. Install dependencies.
2. Run `make` to generate the parser code used by `extract_fw.py`.
3. Obtain the `fw-*.bin` binaries you're interested in. You can find
   these in the [ath6k][ath6k] directory of the
   [linux-firmware][linux-firmware] repo.
4. Extract the firmware image from each binary with
   `./extract_fw.py ...`, where `...` is the name of the `fw-*.bin`
   firmware binary.


## License

Except where otherwise stated:

* All software in this repository (e.g., tools for downloading and extracting
  firmware, etc.) is made available under the
  [Zero-Clause BSD (0BSD) license][license].
* All copyrightable content that is not software (e.g., reverse engineering
  notes, this README file, etc.) is licensed under the
  [Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].


[ksc]: https://github.com/kaitai-io/kaitai_struct_compiler
[kspr]: https://github.com/kaitai-io/kaitai_struct_python_runtime
[ath6k]: https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/tree/ath6k
[linux-firmware]: https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/
[license]: LICENSE.txt
[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/
