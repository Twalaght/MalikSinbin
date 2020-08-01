#!/usr/bin/python3

weight = input("Enter weight: ")
reps = input("Enter reps: ")

onerep = round(int(weight) * (1 + (int(reps) / 30)), 1)

print("\nEstimated one rep max is: " + str(onerep) + "kg\n")

print(" - Use " + str(round(0.5 * onerep, 1)) + "kg for explosive power")
print(" - Use " + str(round(0.7 * onerep, 1)) + "kg for endurance")
print(" - Use " + str(round(0.8 * onerep, 1)) + "kg for muscle")
print(" - Use " + str(round(0.9 * onerep, 1)) + "kg for power")
print(" - Use " + str(round(0.95 * onerep, 1)) + "kg for strength")
