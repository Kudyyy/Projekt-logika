#!/usr/bin/env python

import subprocess,sys

n = ( 0, 5, 10, 15, 20, 25, 4, 8, 3, 1, -2, -5, -10, -11, -15, -15 )
m = ( 1, 0, 10, 5, 5, 11, 5, 15, -2, 20, 10, -2, 0, 0, -15, -21 )
r = ( 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)

for index in range(len(r)):
	str_n = str(n[index])
	str_m = str(m[index])
	exec_str = "\npython conditions.py "+str_n+" "+str_m
	print exec_str
	print "input values:\n",str_n," ", str_m
	print "output value:"
	subprocess.call([exec_str],shell=True)
	print "expected value:\n",r[index]



