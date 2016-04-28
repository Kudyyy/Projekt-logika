#!/usr/bin/python

import sys

assert len(sys.argv) == 8, "Prosze podac 7 argumentow ktore sa liczbami"

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d = int(sys.argv[4])
e = int(sys.argv[5])
f = int(sys.argv[6])
g = int(sys.argv[7])

if ( ( a > 0 and b > 0 and (c % 2 == 1 or d % 2 == 1) and e % 5 == 0) or (f < -10 and g < f ) ):
  print 1
else:
  print 0


