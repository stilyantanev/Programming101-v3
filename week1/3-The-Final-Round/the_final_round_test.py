import unittest
from count_words import count_words
from unique_words_count import unique_words_count
from nan_expand import nan_expand
from iterations_of_nan_expand import iterations_of_nan_expand
from prime_factorization import prime_factorization
from group import group
from max_consecutive import max_consecutive
from groupby import groupby
from prepare_meal import prepare_meal
from reduce_file_path import reduce_file_path
from is_an_bn import is_an_bn
from is_credit_card_valid import is_credit_card_valid
from goldbach import goldbach
from magic_square import magic_square
from friday_years import friday_years


class TheFinalRoundTest(unittest.TestCase):
    def test_count_words(self):
        result = {
            "bear": 1,
            "boar": 2,
            "cat": 1,
        }
        self.assertEqual(count_words(["bear", "boar", "cat", "boar"]), result)

    def test_unique_words_count(self):
        result = ["flower", "dust", "flower", "star", "commet", "star"]
        self.assertEqual(unique_words_count(result), 4)

    def test_nan_expand(self):
        self.assertEqual(nan_expand(0), "")
        self.assertEqual(nan_expand(1), "Not a NaN")
        self.assertEqual(nan_expand(2), "Not a Not a NaN")

    def test_iterations_of_nan_expand(self):
        self.assertNotEqual(iterations_of_nan_expand(""), 1)
        self.assertEqual(iterations_of_nan_expand("Not a Not a NaN"), 2)
        self.assertFalse(iterations_of_nan_expand("Different test"))

    def test_prime_factorization(self):
        self.assertEqual(prime_factorization(20), [(2, 2), (5, 1)])
        self.assertEqual(prime_factorization(4), [(2, 2)])
        self.assertEqual(prime_factorization(100), [(2, 2), (5, 2)])

    def test_group(self):
        self.assertEqual(group([2, 2, 2, 1, 1, 2]), [[2, 2, 2], [1, 1], [2]])
        self.assertEqual(group([1, 2, 3, 4, 5]), [[1], [2], [3], [4], [5]])
        self.assertNotEqual(group([2, 2, 2, 1]), [2, 2, 2, 2])

    def test_max_consecutive(self):
        self.assertEqual(max_consecutive([0, 0, 0, 0, 1, 1, 1]), 4)
        self.assertEqual(max_consecutive([0, 10, 4, 15, 1, 2]), 1)
        self.assertEqual(max_consecutive([]), 0)

    def test_group_by(self):
        result = {
            False: [0, 1, 3, 4, 5],
            True: [2],
        }
        self.assertEqual(groupby(lambda x: x == 2, [0, 1, 2, 3, 4, 5]), result)

    def test_prepare_meal(self):
        self.assertEqual(prepare_meal(8), "\"\"")
        self.assertEqual(prepare_meal(225), '\"spam spam and eggs\"')
        self.assertEqual(prepare_meal(15), '\"spam and eggs\"')

    def test_reduce_file_path(self):
        self.assertEqual(reduce_file_path("/file/../folder/.././"), "/")
        self.assertEqual(reduce_file_path("/C://folder/.//"), "/C:/folder")
        self.assertEqual(reduce_file_path("/D:/prog/file///"), "/D:/prog/file")
        self.assertEqual(reduce_file_path("//file//../"), "/")

    def test_is_an_bn(self):
        self.assertTrue(is_an_bn(""))
        self.assertTrue(is_an_bn("aaaaabbbbb"))
        self.assertFalse(is_an_bn("aaaaabbbb"))
        self.assertTrue(is_an_bn("aaabbb"))
        self.assertFalse(is_an_bn("bbbaa"))
        self.assertTrue(is_an_bn("ab"))

    def test_is_credit_card_valid(self):
        self.assertTrue(is_credit_card_valid(79927398713))
        self.assertFalse(is_credit_card_valid(79299191913))
        self.assertFalse(is_credit_card_valid(5926826828))

    def test_goldbach(self):
        self.assertEqual(goldbach(50), [(3, 47), (7, 43), (13, 37), (19, 31)])
        self.assertEqual(goldbach(25), [(2, 23)])

    def test_magic_square(self):
        self.assertTrue(magic_square([[2, 7, 6], [9, 5, 1], [4, 3, 8]]))
        self.assertFalse(magic_square([[3, 5, 8], [9, 2, 8], [1, 6, 7]]))
        self.assertFalse(magic_square([[7, 3, 4], [4, 1, 1], [4, 1, 2]]))

    def test_friday_years(self):
        self.assertEqual(friday_years(1100, 2100), 177)
        self.assertEqual(friday_years(1801, 2000), 36)
        self.assertEqual(friday_years(2004, 2005), 1)

if __name__ == '__main__':
    unittest.main()
