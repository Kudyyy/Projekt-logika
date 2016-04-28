#!/usr/bin/python

import sys

n = int(sys.argv[1])
m = int(sys.argv[2])

if ( ( n <= 0 or m <= 0 or (n % 2 != 1 and m % 2 != 1) or n % 5 != 0) and (n >= -10 or m >= n ) ):
  print 1
else:
  print 0

