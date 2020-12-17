#!/usr/bin/python3

import time

arry = "POLICE ASSAULT IN PROGRESS  ///  "
index = 0
length = 20

while True:
    index %= len(arry)

    print("[ ", end="")

    if index + length > len(arry):
        print(arry[index:], end="")
        print(arry[:length - len(arry) + index], end="")
    else:
        print(arry[index:index + length], end="")

    print(" ] Δ", end="\r")

    index += 1
    time.sleep(0.08)
