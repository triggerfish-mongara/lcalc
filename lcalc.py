#!/usr/bin/env python3

import readline
import re

def insert_underscores(in_str):
    """
    Return the argument separating with '_' on each 4 characters form the head
    """
    new_str = ""
    for i in range(0, len(in_str), 4):
        new_str = new_str + in_str[i:i + 4] + ('_' if i != len(in_str) - 4 else '')
    return new_str

def to_hex(val):
    """
    Receive int and return a string in hexadecimal. Padded by 32 bits considering 2's complement for negative values
    """
    COMMON_DIGITS = 8
    val_str = "{:x}".format(val) # Count '-' in negative case
    padded_len = len(val_str) + ((COMMON_DIGITS - (len(val_str) % COMMON_DIGITS)) % COMMON_DIGITS)
    if val < 0:
        val_2_complement = val & ((1 << (padded_len * 4)) - 1)
        final_val_str = "{:x}".format(val_2_complement)
    else:
        final_val_str = "0" * (padded_len - len(val_str)) + val_str
    return(final_val_str)

def to_bin(val):
    """
    Receive int and return a string in binary. Padded by 32 bits considering 2's complement for negative values
    """
    COMMON_DIGITS = 32
    val_str = "{:b}".format(val) # Count '-' in negative case
    padded_len = len(val_str) + ((COMMON_DIGITS - (len(val_str) % COMMON_DIGITS)) % COMMON_DIGITS)
    if val < 0:
        val_2_complement = val & ((1 << padded_len) - 1)
        final_val_str = "{:b}".format(val_2_complement)
    else:
        final_val_str = "0" * (padded_len - len(val_str)) + val_str
    return(final_val_str)

def print_bin(header_text, body_text):
    CHARS_IN_A_CHUNK = 32 + 8 # 32digits and 8 underscores 
    for i in range(0, len(body_text), CHARS_IN_A_CHUNK):
        if (i == 0):
            print_header = header_text
        else:
            print_header = " " * len(header_text)
        print(print_header, body_text[i:i + CHARS_IN_A_CHUNK - 1])

def main():
    while True:
        try:
            inp=input("Lcalc > ")
        except:
            print()
            exit()
        try:
            res=eval(inp)
        except:
            print ("Wrong input") 
            continue

        if not isinstance(res, (int, float)):
            print ("Wrong input") 
            continue
            
        print("(DEC) {:,}".format(res))
        print("(HEX)", insert_underscores(to_hex(int(res))))
        print_bin("(BIN)", insert_underscores(to_bin(int(res))))

main()

