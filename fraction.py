"""Fraction library"""

# pylint: disable=invalid-name

import copy

def gcd(a,b):
    """Greatest Common Denominator"""
    if a<0:
        a*=-1
    if b<0:
        b*=-1
    if a==0:
        return b
    return gcd(b%a,a)

def lcm(a,b):
    """Least Common Denominator"""
    return a*b/gcd(a,b)

class Fraction():
    """Fraction manipulation class"""
    prettyFlag=True # class variable
    def __init__(self,numerator,denominator=None):
        if isinstance(numerator,Fraction):
            # "copy constructor"
            self.num=numerator.num
            self.den=numerator.den
            return
        if not isinstance(numerator,int):
            raise Exception('Fraction.__init__(): numerator must be int')
        if denominator is None:
            denominator=1
        elif not isinstance(denominator,int):
            raise Exception('Fraction.__init__(): denominator must be int')
        if numerator<0 and denominator<0:
            self.num=-1*numerator
            self.den=-1*denominator
        else:
            self.num=numerator
            self.den=denominator

    def cc(self):
        """Shorthand for copy.deepcopy()"""
        return copy.deepcopy(self)

    @staticmethod
    def prettyprint(to=None):
        """Set prettyprint to True or False"""
        if to is None:
            return Fraction.prettyFlag
        if not isinstance(to,bool):
            raise Exception('Fraction.prettyprint(): parameter must be bool')
        Fraction.prettyFlag=to
        return Fraction.prettyFlag

    def __str__(self):
        return '{}/{}'.format(self.num,self.den)

    def __repr__(self):
        return '{}/{}'.format(self.num,self.den)

    def reduct(self):
        """Reduct the fraction"""
        a=gcd(self.num,self.den)
        self.num//=a
        self.den//=a
        return self

    def pretty(self):
        """Pretty print the value"""
        self.reduct()
        if self.num<0:
            signed=True
            num=-self.num
        else:
            signed=False
            num=self.num
        if self.den<0:
            signed=not signed
            den=-1*self.den
        else:
            den=self.den
        if signed:
            s='-'
        else:
            s=''
        wh=num//den
        num=num%den
        if wh:
            if num:
                return f'{s}{wh} {num}/{den}'
            return f'{s}{wh}'
        return f'{s}{num}/{den}'

    def prt(self):
        """Print or Pretty print the value depending on class variable"""
        if Fraction.prettyFlag:
            return self.pretty()
        return self.__str__()

    def whole(self):
        """Return the whole part of this Fraction instance"""
        return self.num//self.den

    def isWhole(self):
        """Return whether this Fraction instance is a whole"""
        return self.num==0 or self.num%self.den==0

    def asFloat(self):
        """Return this Fraction instance as a float"""
        return self.num/self.den

    def rebase(self,rhs):
        """Rebase self and rhs to common denominator"""
        if isinstance(rhs,int):
            rhs=Fraction(rhs,1)
        elif not isinstance(rhs,Fraction):
            raise Exception('Fraction.rebase(): rhs must be a Fraction')
        if self.den!=rhs.den:
            self.num*=rhs.den
            rhs.num*=self.den
            self.den*=rhs.den
            rhs.den=self.den
        return self

    def __add__(self,rhs):
        if isinstance(rhs,int):
            rhs=Fraction(rhs,1)
        elif not isinstance(rhs,Fraction):
            raise Exception('Fraction.__add__(): rhs must be a Fraction')
        lhs=copy.deepcopy(self)
        if not lhs.num or not lhs.den:
            lhs.num=rhs.num
            lhs.den=rhs.den
            return lhs
        if not rhs.num or not rhs.den:
            return lhs
        i=int(lcm(rhs.den,lhs.den))
        a=lhs.num*i//lhs.den
        b=rhs.num*i//rhs.den
        lhs.num=a+b
        lhs.den=i
        return lhs

    def add(self,rhs):
        """Synonym for plus operator"""
        return self.__add__(rhs)

    def __sub__(self,rhs):
        if isinstance(rhs,int):
            rhs=Fraction(rhs,1)
        elif not isinstance(rhs,Fraction):
            raise Exception('Fraction.__sub__(): rhs must be a Fraction')
        self.rebase(rhs)
        lhs=copy.deepcopy(self)
        lhs.num-=rhs.num
        return lhs.reduct()

    def sub(self,rhs):
        """Synonym for minus operator"""
        return self.__sub__(rhs)

    def __mul__(self,rhs):
        if isinstance(rhs,int):
            rhs=Fraction(rhs,1)
        elif not isinstance(rhs,Fraction):
            raise Exception('Fraction.__mul__(): rhs must be a Fraction')
        if not rhs.den or not self.den:
            raise Exception(
                'Fraction.__mul__(): this or rhs denumerator is zero')
        lhs=copy.deepcopy(self)
        lhs.num*=rhs.num
        lhs.den*=rhs.den
        return lhs.reduct()

    def mul(self,rhs):
        """Synonym for multiply operator"""
        return self.__mul__(rhs)

    def __eq__(self,rhs):
        if isinstance(rhs,int):
            rhs=Fraction(rhs,1)
        elif not isinstance(rhs,Fraction):
            raise Exception('Fraction.__eq__(): rhs must be a Fraction')
        self.reduct()
        rhs.reduct()
        return self.num==rhs.num and self.den==rhs.den

    def eq(self,rhs):
        """Synonym for equal operator"""
        return self.__eq__(rhs)

    def __ne__(self,rhs):
        return not self.__eq__(rhs)

    def ne(self,rhs):
        """Synonym for not equal operator"""
        return self.__ne__(rhs)

    def __lt__(self,rhs):
        if isinstance(rhs,int):
            rhs=Fraction(rhs,1)
        elif not isinstance(rhs,Fraction):
            raise Exception('Fraction.__lt__(): rhs must be a Fraction')
        if self.den==rhs.den:
            return self.num<rhs.num
        self.rebase(rhs)
        return self.num<rhs.num

    def lt(self,rhs):
        """Synonym for less than operator"""
        return self.__lt__(rhs)

    def __gt__(self,rhs):
        if isinstance(rhs,int):
            rhs=Fraction(rhs,1)
        elif not isinstance(rhs,Fraction):
            raise Exception('Fraction.__gt__(): rhs must be a Fraction')
        if self.den==rhs.den:
            return self.num>rhs.num
        self.rebase(rhs)
        return self.num>rhs.num

    def gt(self,rhs):
        """Synonym for greater than operator"""
        return self.__gt__(rhs)

    def __le__(self,rhs):
        if isinstance(rhs,int):
            rhs=Fraction(rhs,1)
        elif not isinstance(rhs,Fraction):
            raise Exception('Fraction.__le__(): rhs must be a Fraction')
        if self.eq(rhs):
            return True
        return self.lt(rhs)

    def le(self,rhs):
        """Synonym for less than or equal operator"""
        return self.__le__(rhs)

    def __ge__(self,rhs):
        if isinstance(rhs,int):
            rhs=Fraction(rhs,1)
        elif not isinstance(rhs,Fraction):
            raise Exception('Fraction.__ge__(): rhs must be a Fraction')
        if self.eq(rhs):
            return True
        return self.gt(rhs)

    def ge(self,rhs):
        """Synonym for greater than or equal operator"""
        return self.__ge__(rhs)
