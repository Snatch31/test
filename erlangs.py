#!/usr/bin/env python

import math

for p in range(1,80+1):
	for c in range(p,p*2+1):
		num=pow(p,c)*1.0/math.factorial(c)
		den=0
		for i in range(0,c):
			den += pow(p,i) * 1.0 / math.factorial(i)
		print(str(c)+" " + str(p) + " " +str(num/den))
