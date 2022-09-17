from functools import cache

@cache
# Without Memoization == 2 ** n Time Complexity
def SimpleFibanacci(n):
    if n <= 2:
        return 1
    
    return SimpleFibanacci(n-1) + SimpleFibanacci(n-2)

print(SimpleFibanacci(6))
print(SimpleFibanacci(7))
print(SimpleFibanacci(8))
print(SimpleFibanacci(50))


def NaiveFibanacci(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = NaiveFibanacci(n-1) + NaiveFibanacci(n-2)
    return result

print(NaiveFibanacci(6))
print(NaiveFibanacci(7))
print(NaiveFibanacci(8))


    
""" else:
        result = Fibanacci(n - 1) + Fibanacci(n - 2)
    return result """
