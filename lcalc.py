#!/usr/bin/env python3

import readline

def printInHex(val):
    """
    Print argument in hexdecimal, separating by '_' each 4 chars. Value is transformed to 2's complement.
    """
    COMMON_DIGITS = 8
    val_str = "{:x}".format(val) # Count '-' in negative case
    padded_len = len(val_str) + ((COMMON_DIGITS - (len(val_str) % COMMON_DIGITS)) % COMMON_DIGITS)
    if val < 0:
        val_2_complement = val & ((1 << (padded_len * 4)) - 1)
        final_val_str = "{:x}".format(val_2_complement)
    else:
        final_val_str = "0" * (padded_len - len(val_str)) + val_str
    f_hex_res=[]
    for idx, c in enumerate(reversed(final_val_str)):
        if idx != 0 and idx % 4 == 0:
            f_hex_res.insert(0, '_')
        f_hex_res.insert(0, c)
    print("(HEX) " + ''.join(f_hex_res))

def printInBin(val):
    """
    Print argument in binary, speparating by '_' each 4 chars. Value is transformed to 2's complement
    """
    COMMON_DIGITS = 32
    val_str = "{:b}".format(val) # Count '-' in negative case
    padded_len = len(val_str) + ((COMMON_DIGITS - (len(val_str) % COMMON_DIGITS)) % COMMON_DIGITS)
    if val < 0:
        val_2_complement = val & ((1 << padded_len) - 1)
        final_val_str = "{:b}".format(val_2_complement)
    else:
        final_val_str = "0" * (padded_len - len(val_str)) + val_str
    f_bin_res=[]
    for idx, c in enumerate(reversed(final_val_str)):
        if idx != 0:
            if idx % 32 == 0:
                f_bin_res.insert(0, '\n      ')
            elif idx != 0 and idx % 4 == 0:
                f_bin_res.insert(0, '_')
        f_bin_res.insert(0, c)
    print("(BIN) " + ''.join(f_bin_res))

def main():
    while True:
        inp=input("Calc > ")
        try:
            res=eval(inp)
        except:
            print ("Wrong input") 
            continue

        if not isinstance(res, int):
            print ("Wrong input") 
            continue
            
        print("(DEC) {:,}".format(res))
        printInHex(int(res))
        printInBin(int(res))

main()

