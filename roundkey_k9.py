# -*- coding: utf-8 -*-
"""RoundKey_K9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13K8ev8hLZzvdunFANqlGtCcFildFfgub
"""

IPI1 = [3, 0, 4, 19, 20, 23, 2, 1, 5, 18, 21, 22, 6, 9, 10, 13, 14, 17, 7, 8, 11, 12, 15, 16]
IPI2 = [0, 1, 6, 7, 2, 3, 8, 9, 4, 5, 10, 11, 13, 14, 19, 18, 12, 15, 20, 21, 16, 17, 22, 23]
IPI3 = [6, 14, 4, 19, 18, 3, 7, 15, 5, 23, 22, 2, 10, 9, 12, 13, 0, 20, 11, 8, 17, 16, 1, 21]


# Inverse Bit-Permutation with PI2
def IBPL2(x):
    y = [False for _ in range(24)]
    for i in range(0, 24):
        y[i] = x[IPI2[i]]
    for i in range(0, 24):
        x[i] = y[i]

# Inverse Linear Mixing Layer in Data Path: inv_theta_d
def ILML1(x):
    y = [False for _ in range(24)]
    for i in range(0, 24):
        y[i] = x[(i + 8) % 24] ^ x[(i + 20) % 24] ^ x[(i + 22) % 24]
    for i in range(0, 24):
        x[i] = y[i]

# Inverse Bit-Permutation with IPI1
def IBPL1(x):
    y = [False for _ in range(24)]
    for i in range(0, 24):
        y[i] = x[IPI1[i]]
    for i in range(0, 24):
        x[i] = y[i]

def ISBL(x):
    IBBB = [0x00, 0x01, 0x02, 0x03, 0x04, 0x31, 0x05, 0x3a, 0x08, 0x12, 0x35, 0x26, 0x13, 0x36, 0x0a, 0x2c, 0x2e,
            0x09, 0x38, 0x15, 0x33, 0x14, 0x3e, 0x0b, 0x2b, 0x10, 0x25, 0x3c, 0x11, 0x21, 0x23, 0x29, 0x2f, 0x27,
            0x3f, 0x37, 0x34, 0x1a, 0x1d, 0x39, 0x30, 0x2a, 0x1f, 0x0c, 0x19, 0x0f, 0x28, 0x3d, 0x24, 0x18, 0x3b,
            0x0d, 0x20, 0x0e, 0x1e, 0x22, 0x1b, 0x32, 0x1c, 0x17, 0x07, 0x16, 0x06, 0x2d]

    for j in range(0, 4):
        i = 6 * j + 5
        a = 1 if x[i] == 1 else 0
        for k in range(5):
            i -= 1
            a <<= 1
            a ^= 1 if x[i] == 1 else 0
        a = IBBB[a]
        i = 6 * j + 5
        for k in range(6):
            x[i - k] = (a >> (5 - k)) & 1

def IRFC(x):
    IBPL2(x)
    ILML1(x)
    IBPL1(x)
    ISBL(x)

# Inverse Bit-Permutation with PI3
def IBPL3(x):
    y = [False for _ in range(24)]
    for i in range(0, 24):
        y[i] = x[IPI3[i]]
    for i in range(0, 24):
        x[i] = y[i]


# Input
x = [int(bit) for bit in "110010101000010110110001"]

# Apply RFS
IRFC(x)

# Output
output = ''.join(map(str, x))


correct_round9 = '101101010010011011110011'
faulty_round9  = '110000101010001011011101'
real_k9 = '001100101011100000001000'
k9_list =[]
k9_list_valid =[]


for j in range(2**24):
    k9_list.append(format(j, '024b'))

for k9 in k9_list:
  result2 = int(k9, 2) ^ int(faulty_round9, 2)
  result2_h = format(result2, '024b')
  input_list_faulty = [int(bit) for bit in result2_h]
  IBPL3(input_list_faulty)
  ISBL(input_list_faulty)
  IBPL2(input_list_faulty)
  ILML1(input_list_faulty)
  output_binary_faulty = ''.join(map(str, input_list_faulty))
  bit_selected_faulty = output_binary_faulty[6:18]

  #print(bit_selected_faulty)

  result2_c = int(k9, 2) ^ int(correct_round9, 2)
  result2_h_c = format(result2_c, '024b')
  input_list_correct = [int(bit) for bit in result2_h_c]
  IBPL3(input_list_correct)
  ISBL(input_list_correct)
  IBPL2(input_list_correct)
  ILML1(input_list_correct)
  output_binary_correct = ''.join(map(str, input_list_correct))
  bit_selected_correct= output_binary_correct[6:18]

  #print(bit_selected_correct)

  if bit_selected_faulty == bit_selected_correct:
    k9_list_valid.append(k9)

print("len k9 list valid",len(k9_list_valid))