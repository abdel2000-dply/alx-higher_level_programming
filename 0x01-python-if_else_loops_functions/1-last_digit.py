#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdg = abs(number) % 10
if number < 0:
    lastdg = - lastdg
print("Last digit of", number, "is", lastdg, end=" ")

if lastdg > 5:
    print("and is greater than 5")
elif lastdg == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
