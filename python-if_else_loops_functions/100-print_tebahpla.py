#!/usr/bin/python3

for i in range(13):
    print(chr(ord('z') - (i * 2)), end="")
    print(chr(ord('z') - (i * 2 + 1)).upper(), end="")
