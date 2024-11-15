import numpy as np

def twopack(arr, bitlength=4):
    paired_unpacked = arr.reshape(-1, 2)
    packed = (paired_unpacked[:, 0] << bitlength) + paired_unpacked[:, 1]
    return packed

def twounpack(arr, bitlength=4):
    unpacked = np.zeros((arr.size * 2), dtype=np.uint8)
    unpacked[1::2] = arr & (2**bitlength - 1)
    unpacked[::2] = arr >> (bitlength)
    return unpacked.flatten()