#!/usr/bin/python

import os
import json

path = "/home/pi/.guardian/"

file = open(path+"account","r")

account = json.load(file)

print "You have "+str(account["balance"])+" seconds in your account."

pocket=0

deduction=path+"deducted"

if os.path.exists(deduction):
    with open(deduction) as file:
        pocket=int(next(file))

print "You have "+str(pocket)+" seconds in your pocket."
