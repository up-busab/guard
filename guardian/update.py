#!/usr/bin/python

import sys;
import json;

path = "/home/pi/.guardian/"
filepath = path+"account"

def update(amount):

	with open(filepath,"r") as file:
		account = json.load(file)

	balance = account["balance"] + amount

	if(balance>=0):
		account["balance"] = balance
		with open(filepath,"w") as file:
			json.dump(account,file)
	else:
		amount = 0

	return amount

if __name__ == "__main__":
	exit(update(int(sys.argv[1])))
