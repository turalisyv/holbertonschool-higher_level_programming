#!/usr/bin/python3

for i in range(0, 100):
    if "{:02d}".format(i) != "99":
        print("{:02d}".format(i), end=", ")

    else:
        print("99")
