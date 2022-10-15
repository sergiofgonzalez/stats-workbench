from math import gcd, factorial
import logging

logger = logging.getLogger("Fraction")


class Fraction:
    def __init__(self, numerator, denominator=1):
        logger.debug(f"About to construct Fraction({numerator}, {denominator})")

        if not Fraction.__isValidIntArgs(numerator, denominator):
            raise TypeError("Fractional expects integer arguments")

        if denominator == 0:
            raise ValueError("Fractional expects non-zero denominator")

        greatest_common_divisor = gcd(abs(numerator), abs(denominator))

        self.numerator = numerator // greatest_common_divisor
        self.denominator = denominator // greatest_common_divisor

        logger.debug(f"Fraction({self.numerator}, {self.denominator}) constructed")

    def add(self, other):
        if not isinstance(other, (int, Fraction)):
            raise TypeError("Fractional.add expects an int or a Fraction")

        other_as_fraction = other
        if isinstance(other, int):
            other_as_fraction = Fraction(other)

        return Fraction(
            self.numerator * other_as_fraction.denominator + other_as_fraction.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    def mult(self, other):
        if not isinstance(other, (int, Fraction)):
            raise TypeError("Fractional.mult expects and int or a Fraction")

        other_as_fraction = other
        if isinstance(other, int):
            other_as_fraction = Fraction(other)

        return Fraction(
            self.numerator * other_as_fraction.numerator,
            self.denominator * other_as_fraction.denominator
        )

    def div(self, other):
        if not isinstance(other, (int, Fraction)):
            raise TypeError("Fractional.div expects and int or a Fraction")

        other_as_fraction = other
        if isinstance(other, int):
            other_as_fraction = Fraction(other)

        return self.mult(Fraction(other_as_fraction.denominator, other_as_fraction.numerator))

    def subtract(self, other):
        if not isinstance(other, (int, Fraction)):
            raise TypeError("Fractional.subtract expects and int or a Fraction")

        other_as_fraction = other
        if isinstance(other, int):
            other_as_fraction = Fraction(other)

        return self.add(other_as_fraction.mult(-1))

    def lessThan(self, other):
        if not isinstance(other, (int, Fraction)):
            raise TypeError('Rational.lessThan expects an integer or Rational')

        other_as_fraction = other
        if isinstance(other, int):
            other_as_fraction = Fraction(other)

        return self.numerator * other_as_fraction.denominator < other_as_fraction.numerator * self.denominator

    def lessOrEqualThan(self, other):
        if not isinstance(other, (int, Fraction)):
            raise TypeError('Rational.lessOrEqualThan expects an integer or Rational')

        other_as_fraction = other
        if isinstance(other, int):
            other_as_fraction = Fraction(other)

        return self.numerator * other_as_fraction.denominator <= other_as_fraction.numerator * self.denominator

    def greaterThan(self, other):
        if not isinstance(other, (int, Fraction)):
            raise TypeError('Rational.greaterThan expects an integer or Rational')

        other_as_fraction = other
        if isinstance(other, int):
            other_as_fraction = Fraction(other)

        return self.numerator * other_as_fraction.denominator > other_as_fraction.numerator * self.denominator

    def greaterOrEqualThan(self, other):
        if not isinstance(other, (int, Fraction)):
            raise TypeError('Rational.greaterOrEqualThan expects an integer or Rational')

        other_as_fraction = other
        if isinstance(other, int):
            other_as_fraction = Fraction(other)

        return self.numerator * other_as_fraction.denominator >= other_as_fraction.numerator * self.denominator

    def power(self, exponent):
        if not isinstance(exponent, int):
            raise TypeError('Rational.power expects an integer exponent')

        return Fraction(self.numerator ** exponent, self.denominator ** exponent)

    def __add__(self, other):
        return self.add(other)

    def __radd__(self, other):
        if not isinstance(other, (int, Fraction)):
            raise TypeError('Rational.__radd__ expects an integer or Rational')

        other_as_fraction = other
        if isinstance(other, int):
            other_as_fraction = Fraction(other)

        return other_as_fraction.add(self)

    def __sub__(self, other):
        return self.subtract(other)

    def __rsub__(self, other):
        if not isinstance(other, (int, Fraction)):
            raise TypeError('Fraction.__rsub__ expects an integer or Rational')

        other_as_fraction = other
        if isinstance(other, int):
            other_as_fraction = Fraction(other)

        return other_as_fraction.subtract(self)

    def __mul__(self, other):
        return self.mult(other)

    def __rmul__(self, other):
        if not isinstance(other, (int, Fraction)):
            raise TypeError('Fraction.__rmul__ expects an integer or Rational')

        other_as_fraction = other
        if isinstance(other, int):
            other_as_fraction = Fraction(other)

        return other_as_fraction.mult(self)

    def __truediv__(self, other):
        return self.div(other)

    def __eq__(self, other):
        if self.__class__ not in other.__class__.mro():
            return False
        else:
            return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        return self.lessThan(other)

    def __le__(self, other):
        return self.lessOrEqualThan(other)

    def __gt__(self, other):
        return self.greaterThan(other)

    def __ge__(self, other):
        return self.greaterOrEqualThan(other)

    def __pow__(self, exponent):
        return self.power(exponent)

    def __repr__(self):
        if self.numerator == 0:
            return str(0)
        elif self.denominator == 1:
            return str(self.numerator)
        else:
            return f"{self.numerator}/{self.denominator}"

    def latex(self):
        if self.numerator == 0:
            return "$ 0 $"
        elif self.denominator == 1:
            return f"$ {self.numerator} $"
        else:
            return f"$ \\frac{{{self.numerator}}}{{{self.denominator}}} $"

    def to_float(self):
        return self.numerator / self.denominator

    @staticmethod
    def __isValidIntArgs(*nums):
        return all([isinstance(num, int) for num in nums])


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s [%(asctime)s]: (%(name)s) %(message)s",
    )
    logging.info("Running some examples...")
    frac = Fraction(2, 4)
    print(frac)
    print(frac.latex())

    # simplifying with huge numbers
    numerator = factorial(4) * factorial(48) * factorial(5)
    denominator = factorial(3) * factorial(2) * factorial(46)
    huge_numbers_frac = Fraction(numerator, denominator)
    print(huge_numbers_frac)
