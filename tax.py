#!/usr/bin/python3
import sys

total = float(sys.argv[1])
originaltotal = total
totaltax = 0

# Add medicare levy
totaltax += 0.02 * total

while total != 0:
    if total <= 18200:
        total = 0
    elif total <= 45000:
        totaltax += (0.19 * (total-18200))
        total = 18200
    elif total <= 120000:
        totaltax += (0.325 * (total-45000))
        total = 45000
    elif total <= 180000:
        totaltax += (0.37 * (total-120000))
        total = 120000
    else:
        totaltax += (0.45 * (total-180000))
        total = 180000


print("Tax: $" + str(totaltax) + " with a average rate of " + str((totaltax/originaltotal)*100) + "%")
