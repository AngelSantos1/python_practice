#import numpy
#Combination - permutation

from math import prod

def choose(n, k):
    num = prod(range(n-k+1, (n)+1))  # numerator
    denom = prod(range(1, (k)+1))    # denominator
    return num // denom

#class Solution:
    #def climbStairs(self, n: int) -> int:
def climbStairs(n):
    out = 0
    # a = number of 1 steps
    # b = number of 2 steps
    for b in range(0, n//2 + 1):
        a = n - 2 * b
        # checks if works
        if a + 2 * b != n:
            #print(a, b, "doesn't works")
            continue
        out += choose(a + b, b)
    print(out)
    #return out
n = 5
climbStairs(n)
#def choose(n,k)


#Matty's Solution
""" from math import prod

def choose(n, k):
    num = prod(range(n-k+1, (n)+1))  # numerator
    denom = prod(range(1, (k)+1))    # denominator
    return num // denom

class Solution:
    def climbStairs(self, n: int) -> int:
        out = 0
        # a = number of 1 steps
        # b = number of 2 steps
        for b in range(0, n//2 + 1):
            a = n - 2 * b
            # checks if works
            if a + 2 * b != n:
                #print(a, b, "doesn't works")
                continue
            out += choose(a + b, b)
        return out """



""" from math import factorial
from math import prod

def combinations(totalNumber, combinations):
    for twoSteps in range(): """