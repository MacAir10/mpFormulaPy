﻿#
#class MyClass:
#	def __init__(self):
#		pass

#    def __init__(self):
#        print sys.path


import sys

for arg in sys.argv:
	sys.path.append(arg);
	
from mpmath import *
from decimal import *
from fractions import *


class MyClass:
    def __init__(self):
        pass

    def pygetmp(self):
    	return mp

    	
    def pympf(self, x):
    	return mpf(x)

    def pympfi(self, x):
    	return iv.mpf(x)


    def pympc(self, z):
    	return mpmathify(z)

    def pympci(self, x, y):
    	return iv.mpf(x), iv.mpf(y)


    def pyMpfiPrec(self,n):
        iv.dps = n


    def mpmathToString(self, x, n):
        return nstr(x, n)
    	
    def pyeval(self, s):
    	return eval(s)

    def pyexec(self, s):
    	Result = 0;
    	exec(s);
    	return Result

    def pyexec2(self, s1, s2):
    	Result = 0;
    	exec(s1);
    	exec(s2);
    	return Result

    def somemethod(self):
        print "in some method"


    def diff2(self, f, x):
        Result = 0
        Result = diff(f, x)
        return Result

    def diff3(self, f, x, n):
        Result = 0
        Result = diff(f, x, n)
        return Result



    def findroot1d(self, f, x2, StrArgs):
        return eval("findroot(f, x2" + StrArgs + ")")


    def nsum1d(self, f, x2, StrArgs):
        return eval("nsum(f, x2" + StrArgs + ")")

    def nsum2d(self, f, x2, x3, StrArgs):
        return eval("nsum(f, x2, x3" + StrArgs + ")")

    def nsum3d(self, f, x2, x3, x4,StrArgs):
        return eval("nsum(f, x2, x3, x4" + StrArgs + ")")


    def quad1d(self, f, x2, StrArgs):
        return eval("quad(f, x2" + StrArgs + ")")

    def quad2d(self, f, x2, x3, StrArgs):
        return eval("quad(f, x2, x3" + StrArgs + ")")

    def quad3d(self, f, x2, x3, x4,StrArgs):
        return eval("quad(f, x2, x3, x4" + StrArgs + ")")



    def nsumTest(self, f, *x):
        print "starting in nsumTest.py"
        Result = 0
        Result =  nsum(f, *x)
        return Result


    def isodd(self, n):
        return 1 == n % 2

    def pySetDecimalPrec(self,n):
        getcontext().prec = n

    def pyDecimal(self, x):
    	return Decimal(x)

    def pyDecimalString(self, x):
    	return Decimal(x).to_eng_string()

    def pyFraction(self, x):
    	return Fraction(x)

    def pyFractionString(self, x):
    	return Fraction(x).__str__()

    def pyLong(self, x):
    	return long(x)

    def pyLongString(self, x):
    	return long(x).__str__()

