from fractions import gcd


class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        if self.denominator != 1:
            return "{} / {}".format(self.numerator, self.denominator)
        elif self.denominator == 1 or self.numerator == 0:
            return "{}".format(self.numerator)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        first_fraction = self.numerator / self.denominator
        second_fraction = other.numerator / other.denominator

        return first_fraction == second_fraction

    def __add__(self, other):
        numerator = self.numerator * other.denominator + \
            other.numerator * self.denominator
        denominator = self.denominator * other.denominator

        greatest_common_divisor = gcd(numerator, denominator)
        numerator = numerator // greatest_common_divisor
        denominator = denominator // greatest_common_divisor

        return Fraction(numerator, denominator)

    def __sub__(self, other):
        numerator = self.numerator * other.denominator - \
            other.numerator * self.denominator
        denominator = self.denominator * other.denominator

        greatest_common_divisor = gcd(numerator, denominator)
        numerator = numerator // greatest_common_divisor
        denominator = denominator // greatest_common_divisor

        return Fraction(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator

        greatest_common_divisor = gcd(numerator, denominator)
        numerator = numerator // greatest_common_divisor
        denominator = denominator // greatest_common_divisor

        return Fraction(numerator, denominator)


def main():
    a = Fraction(1, 2)
    b = Fraction(2, 4)

    print(a == b)  # True
    print(a + b)  # 1
    print(a - b)  # 0
    print(a * b)  # 1 / 4


if __name__ == '__main__':
    main()
