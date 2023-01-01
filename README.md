# fraction
A fraction manipulation class

The class maintains accurate fractional values. 

Note that the integral num(erator) and den(ominator) member values may get altered by any of the methods as a side effect, e.g. num=2, den=6 may get changed to num=1, den=3. The fraction's value still stays correct, i.e. in this example "one third".

Note that copies of Fraction objects are by default shallow, which may or may not be suitable for intended use. To deep copy Fraction objects, use e.g. the following practice:

from fraction import Fraction as Fra

a = Fra(1,2)
b = Fra(a) # alternatively b = a.cc()
