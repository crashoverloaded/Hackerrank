#!/usr/bin/python3

import numpy as np 

# Seed Is the starting of Random Algorithm We can choose any number
np.random.seed(int(input("Enter Any No. For Seed:-")))

# 2 is not included, It will show Only 0 & 1
coin = np.random.randint(0,2)

if coin == 0:
	print("HEADS")
else:
	print("TAILS")
