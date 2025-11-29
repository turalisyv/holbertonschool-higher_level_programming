#!/usr/bin/python3

for i in range(0, 100):
    if f"{i:02d}" != "99":
        print(f"{i:02d}", end=", ")

    else:
        print("99")
