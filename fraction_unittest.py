'''
Unit tests for Fraction.
Run with
python -m unittest fraction_unittest.py
'''

# pylint: disable=invalid-name,too-many-statements
# pylint: disable=missing-function-docstring,missing-class-docstring

import unittest
from fraction import Fraction as Fra

class TestFraction(unittest.TestCase):
    def testA(self):
        a=Fra(1,4)
        a*=Fra(5,4)
        self.assertEqual(Fra(5,16),a)
        a+=Fra(1,4)
        a+=Fra(1,4)
        a+=Fra(1,16)
        a+=Fra(1,16)
        a+=Fra(1,16)
        self.assertEqual(Fra(1),a)

    def testB(self):
        a=Fra(1,4)
        a*=Fra(9,8)
        self.assertEqual(Fra(9,32),a)
        a+=Fra(1,4)
        a+=Fra(1,4)
        a+=Fra(1,8)
        a+=Fra(1,16)
        a+=Fra(1,32)
        self.assertEqual(Fra(32,32),a)

    def testC(self):
        a=Fra(1,4)
        a*=Fra(17,16)
        self.assertEqual(Fra(17,64),a)
        a+=Fra(1,4)
        a+=Fra(1,4)
        a+=Fra(1,8)
        a+=Fra(1,16)
        a+=Fra(1,32)
        a+=Fra(1,64)
        self.assertEqual(Fra(1),a)

    def testD(self):
        a=Fra(13,32)
        a+=Fra(6,64)
        a+=Fra(1,32)
        b=Fra(1,32)
        b*=Fra(3,2)
        a+=b
        self.assertEqual(Fra(37,64),a)
        a+=Fra(1,4)
        self.assertEqual(Fra(53,64),a)
        a+=Fra(1,8)
        self.assertEqual(Fra(61,64),a)
        a+=Fra(1,32)
        self.assertEqual(Fra(63,64),a)

    def testE(self):
        a=Fra(1,4)
        aa=a.cc()
        aaa=Fra(aa)
        aa+=Fra(3,1)
        aaa*=Fra(1,8)
        self.assertEqual(Fra(1,4),a)
        self.assertEqual(Fra(3*4+1,4),aa)
        self.assertEqual(Fra(1,32),aaa)
        b=Fra(3,4)
        c=a-b
        self.assertEqual(Fra(-1,2),c)
        d=Fra(0)
        self.assertTrue(c<d)
        self.assertFalse(d<c)
        self.assertEqual('1/4',a.pretty())
        self.assertEqual('3/4',b.pretty())
        self.assertEqual('-1/2',c.pretty())
        self.assertEqual(-0.5,c.asFloat())
        self.assertEqual('0/1',d.pretty())
        a=Fra(-2,3)
        self.assertEqual('-2/3',f'{a}')
        self.assertEqual('-2/3',a.pretty())
        a=Fra(2,-3)
        self.assertEqual('2/-3',f'{a}')
        self.assertEqual('-2/3',a.pretty())
        a=Fra(-2,-3)
        self.assertEqual('2/3',f'{a}')
        self.assertEqual('2/3',a.pretty())
        a=Fra(4,3)
        self.assertEqual('4/3',f'{a}')
        self.assertEqual('1 1/3',a.pretty())
        a=Fra(-4,3)
        self.assertEqual('-4/3',f'{a}')
        self.assertEqual('-1 1/3',a.pretty())
        self.assertEqual('-1 1/3',a.prt())
        self.assertFalse(Fra.prettyprint(False))
        self.assertEqual('-4/3',a.prt())
        self.assertEqual(-2,a.whole())
        self.assertFalse(a.isWhole())
        a+=Fra(-2,3)
        self.assertTrue(a.isWhole())
        b=Fra(3,4)
        c=Fra(5,11)
        b.rebase(c)
        self.assertEqual('33/44',b.prt())
        self.assertEqual('20/44',c.prt())
        self.assertEqual(Fra(3,4),b)
        self.assertEqual(Fra(5,11),c)
        self.assertEqual('3/4',b.pretty())
        self.assertEqual('5/11',c.pretty())

if __name__ == '__main__':
    unittest.main()
