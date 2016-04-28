#!/usr/bin/env python

import subprocess

a = ( 1, 5, 0, 2, 5, 4, 10, 2, 2, 5)
b = ( 2, 0, -2, 3, 5, 6, 12, 4, 5, 4)
c = ( 3, 5, 4, 5, 4, 7, -11, -15, 4, -20)
d = ( 5, 9, 8, 5, 5, 5, -13, 10, -7, -14)
e = ( 10, 3, 9, 15, 5, 9, 11, 15, -20, 20)
f = ( -11,-20, -10, 2, 6, -11, -12, -9, 8, -11)
g = ( -20,-21, -12, -20, 10, -10,-13, -20, 20, -11)
r = ( 1, 1, 0, 1, 1, 0, 1, 1, 1, 0)

for index in range(len(r)):
	str_a = str(a[index])
	str_b = str(b[index])
	str_c = str(c[index])
	str_d = str(d[index])
	str_e = str(e[index])
	str_f = str(f[index])
	str_g = str(g[index])

	exec_str = "\npython conditions.py "+str_a+" "+str_b+" "+str_c+" "+str_d+" "+str_e+" "+str_f+" "+str_g
	print exec_str
	print "input values:\n",str_a,str_b,str_c,str_d,str_e,str_f,str_g
	print "output value:"
	subprocess.call([exec_str],shell=True)
	print "expected value:\n",r[index]



