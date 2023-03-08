#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastNum = abs(number) % 10
if number < 0:
    lastNum *= -1
if lastNum > 5:
    print("Last digit of {} is {} and is greater than 5"
          .format(number, lastNum))
elif lastNum < 6 and lastNum != 0:
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, lastNum))
else:
    print("Last digit of {} is 0 and is 0".format(number))
