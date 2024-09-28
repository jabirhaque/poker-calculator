from src.table.lookup import *
import ctypes
def evaluate(hand):
    # hands is an array containing 5 card objects, evaluate returns the ranking of hand
    # 1. check if flush
    # 2. if flush, return flushes[bitwise or on rank bit]
    # 3. otherwise, if unique5[bitwise or on rank bit], return result
    # 4. otherwise return hash_values[hash(prime product of prime)]
    if (hand[0].suit & hand[1].suit & hand[2].suit & hand[3].suit & hand[4].suit) != 0:
        return flushes[hand[0].rank_bit | hand[1].rank_bit | hand[2].rank_bit | hand[3].rank_bit | hand[4].rank_bit]
    elif unique5[hand[0].rank_bit | hand[1].rank_bit | hand[2].rank_bit | hand[3].rank_bit | hand[4].rank_bit] != 0:
         return unique5[hand[0].rank_bit | hand[1].rank_bit | hand[2].rank_bit | hand[3].rank_bit | hand[4].rank_bit]
    else:
        return hash_values[hash(hand[0].prime * hand[1].prime * hand[2].prime * hand[3].prime * hand[4].prime)]
def hash(int):
    u = ctypes.c_uint32(int)
    u.value += 0xe91aaa35
    u.value ^= u.value >> 16
    u.value += u.value << 8
    u.value ^= u.value >> 4
    a = ctypes.c_uint32(u.value + (u.value << 2)).value >> 19
    return a ^ hash_adjust[(u.value >> 8) & 0x1ff]
