# lcalc
A CUI calculator for logic engineers, written in Python.

# Demo

```
Lcalc > 0x3ff * 10 + 0b111_0010
(DEC) 10,344
(HEX) 0000_2868
(BIN) 0000_0000_0000_0000_0010_1000_0110_1000

Lcalc > 1024 * -1
(DEC) -1,024
(HEX) ffff_fc00
(BIN) 1111_1111_1111_1111_1111_1100_0000_0000

Lcalc > 0xffff_ffff * 0xffff_ffff * 0xffff_ffff
(DEC) 79,228,162,458,924,105,385,300,197,375
(HEX) ffff_fffd_0000_0002_ffff_ffff
(BIN) 1111_1111_1111_1111_1111_1111_1111_1101
      0000_0000_0000_0000_0000_0000_0000_0010
      1111_1111_1111_1111_1111_1111_1111_1111

Lcalc > 11 >> 1
(DEC) 5
(HEX) 0000_0005
(BIN) 0000_0000_0000_0000_0000_0000_0000_0101    
```

# Features
* Always display the result in three base numbers - dec, hex, and bin
* No limit for numbers of digits
* Accept input numbers in dec, hex and bin
* Can separate the input number with '\_' at any position. e.g. 0x2_ff3_4430
* Automatically convert the result to 2's complement for hex and bin expressions if it is negative
* Support all Python 3 operators for int (Actually calculation engine is Python itself)
* If the result has fraction (generated by such a operator like >>), it will be rounded down for hex and bin expressions
* Command history available

# Requirement
Python 3

# Installation
Just place lcalc.py anywhere you like and run it.




