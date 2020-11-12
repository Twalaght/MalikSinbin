#!/usr/bin/python3

import sys

# TODO - Handle weights smaller than 20
if len(sys.argv) < 2:
    exit()

total = round(float(sys.argv[1]) / 2.5) * 2.5 - 20

disp = "Total: " + str(total + 20) + " kg"

weights = [50, 40, 30, 20, 10, 5, 2.5]

final = []

while total > 0:
    for i in range(3):
        if total % weights[i] == 0:
            for _ in range(int(total / weights[i])):
                final.append(weights[i]/2)
                total = 0

    i = 0
    while i < 7:
        if total - weights[i] >= 0:
            final.append(weights[i]/2)
            total -= weights[i]
            if total == 0:
                break
            else:
                i = 0
        else:
            i += 1


cols = {
    25   : '\033[41m',
    20   : '\033[44m',
    15   : '\033[43m',
    10   : '\033[42m',
    5    : '\033[47m',
    2.5  : '\033[101m',
    1.25 : '\033[100m'
}

red = '\033[41m'
blue = '\033[44m'
yellow = '\033[43m'
green = '\033[42m'
grey = '\033[47m'
lred = '\033[101m'
endc = '\033[0m'


for i in range(5):
    for j in reversed(range(len(final))):
        if i == 2:
            print('\033[100m' + " " + endc, end="")
        else:
            print(" ", end="")
        print(cols[final[j]] + "   " + endc, end="")

    if i == 1:
        print(disp.center(25), end="")
    elif i == 2:
        print('\033[100m' + "                         " + endc, end="")
    else:
        print("                         " + endc, end="")

    for j in range(len(final)):
        print(cols[final[j]] + "   " + endc, end="")
        if i == 2:
            print('\033[100m' + " " + endc, end="")
        else:
            print(" ", end="")

    print("")
