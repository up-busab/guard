#!/usr/bin/python

import os
import sys

dir = "/home/pi/.guardian/"

sys.path.insert(0,dir)
import update

execfile(dir+"balance.py")

print "--------------------------------------------------"
amount = input("How many seconds would you like to withdraw? ")
print "--------------------------------------------------"

if amount >= 0:
	amount = update.update(-1*amount)
else:
	amount = 0

pocket=0

deduction=path+"deducted"

if os.path.exists(deduction):
    with open(deduction) as file:
        pocket=int(next(file))

with open(dir+"deducted","w+") as file:
    file.write(str(-1*amount+pocket))

execfile(dir+"balance.py")
