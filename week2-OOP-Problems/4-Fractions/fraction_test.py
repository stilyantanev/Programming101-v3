import unittest
from fraction import Fraction
from fractions import gcd


class FractionTest(unittest.TestCase):

    def setUp(self):
        self.fraction = Fraction(1, 2)

    def test_create_new_fraction_instance(self):
        self.assertTrue(isinstance(self.fraction, Fraction))

    def test_members_of_instance(self):
        self.assertEqual(self.fraction.numerator, 1)
        self.assertEqual(self.fraction.denominator, 2)

    def test_str_cast(self):
        self.other_fraction = Fraction(33, 1)
        self.assertEqual(str(self.fraction), "1 / 2")
        self.assertEqual(str(self.other_fraction), "33")

    def test_repr_cast(self):
        self.other_fraction = Fraction(33, 1)
        self.assertEqual(str(self.fraction), "1 / 2")
        self.assertEqual(str(self.other_fraction), "33")

    def test_equals(self):
        self.other_fraction = Fraction(20, 40)

        first_numerator = self.fraction.numerator
        first_denominator = self.fraction.denominator
        first_fraction = first_numerator / first_denominator

        second_numerator = self.other_fraction.numerator
        second_denominator = self.other_fraction.denominator
        second_fraction = second_numerator / second_denominator

        self.assertEqual(first_fraction, second_fraction)

    def test_addition(self):
        self.other_fraction = Fraction(4, 6)

        first_numerator = self.fraction.numerator
        first_denominator = self.fraction.denominator
        second_numerator = self.other_fraction.numerator
        second_denominator = self.other_fraction.denominator

        numerator = first_numerator * second_denominator + \
            second_numerator * first_denominator
        denominator = first_denominator * second_denominator
        self.assertEqual(numerator, 14)
        self.assertEqual(denominator, 12)

        greatest_common_divisor = gcd(numerator, denominator)
        self.assertEqual(greatest_common_divisor, 2)

        numerator = numerator // greatest_common_divisor
        denominator = denominator // greatest_common_divisor
        self.assertEqual(numerator, 7)
        self.assertEqual(denominator, 6)

        new_fraction = Fraction(numerator, denominator)
        self.assertEqual(new_fraction.numerator, 7)
        self.assertEqual(new_fraction.denominator, 6)

    def test_substraction(self):
        self.other_fraction = Fraction(3, 7)

        first_numerator = self.fraction.numerator
        first_denominator = self.fraction.denominator
        second_numerator = self.other_fraction.numerator
        second_denominator = self.other_fraction.denominator

        numerator = first_numerator * second_denominator - \
            second_numerator * first_denominator
        denominator = first_denominator * second_denominator
        self.assertEqual(numerator, 1)
        self.assertEqual(denominator, 14)

        greatest_common_divisor = gcd(numerator, denominator)
        self.assertEqual(greatest_common_divisor, 1)

        numerator = numerator // greatest_common_divisor
        denominator = denominator // greatest_common_divisor
        self.assertEqual(numerator, 1)
        self.assertEqual(denominator, 14)

        new_fraction = Fraction(numerator, denominator)
        self.assertEqual(new_fraction.numerator, 1)
        self.assertEqual(new_fraction.denominator, 14)

    def test_multiplication(self):
        self.other_fraction = Fraction(10, 3)

        first_numerator = self.fraction.numerator
        first_denominator = self.fraction.denominator
        second_numerator = self.other_fraction.numerator
        second_denominator = self.other_fraction.denominator

        numerator = first_numerator * second_numerator
        denominator = first_denominator * second_denominator
        self.assertEqual(numerator, 10)
        self.assertEqual(denominator, 6)

        greatest_common_divisor = gcd(numerator, denominator)
        self.assertEqual(greatest_common_divisor, 2)

        numerator = numerator // greatest_common_divisor
        denominator = denominator // greatest_common_divisor
        self.assertEqual(numerator, 5)
        self.assertEqual(denominator, 3)

        new_fraction = Fraction(numerator, denominator)
        self.assertEqual(new_fraction.numerator, 5)
        self.assertEqual(new_fraction.denominator, 3)


if __name__ == '__main__':
    unittest.main()
