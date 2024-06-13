# A Low-Latency Tweakable Block Cipher Fault Attack Injection
This repository includes the source code of the tools we used in our paper accepted for "Isecure link": Cryptanalysis of BipBip
## Table of Contents


BipBip is a 24-bit tweakable block cipher with a 40-bit tweak that can be implemented in an ASIC with a 3-cycle delay at a 4.5 GHz clock frequency using current 10 nm CMOS technology. BipBip has a block size of 24 bits, masterkey length of 256 bits, and a tweak length of 40 bits. in this section, we perform the primary description from ciphertext to plaintext. The tweak schedule, the key schedule, and the datapath are the three primary components of BipBip.


DFA (Differential Fault Attack) is based on the injection of errors into a cryptographic algorithm during processing, using correct and incorrect (faulty and non-faulty) ciphertexts to exploit this differential feature. The error is going to be injected in different rounds of the mentioned block cipher and each has its own scenario to investigate the round keys and then the master key under very less complexity that can achieve the real one with excessive search.
