import math


def fact(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def gcb(a, b):
    while b:
        a, b = b, a % b
    return a