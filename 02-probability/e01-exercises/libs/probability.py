from fractions import Fraction
from math import factorial


def combinations(n: int, r: int) -> Fraction:
    numerator = int(factorial(n))
    denominator = int(factorial(r) * factorial(n - r))
    return Fraction(numerator, denominator)
