#!/usr/bin/python

import sys

n = int(sys.argv[1])
m = int(sys.argv[2])

if ( ( n > 0 and m > 0 and (n % 2 == 1 or m % 2 == 1) and n % 5 == 0) or (n < -10 and m < n ) ):
  print 1
else:
  print 0


