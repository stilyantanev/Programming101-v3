import unittest
from bank_account import BankAccount


class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Georgi", 200, "$")

    def test_create_new_bank_account_instance(self):
        self.assertTrue(isinstance(self.account, BankAccount))

    def test_valid_members(self):
        self.assertEqual(self.account.name, "Georgi")
        self.assertEqual(self.account.balance, 200)
        self.assertEqual(self.account.currency, "$")
        self.assertEqual(self.account.operations, ["Account was created"])

    def test_int_cast(self):
        self.assertEqual(int(self.account), 200)

    def test_str_cast(self):
        message = "Bank account for {} with balance of {}{}"
        message = message.format("Georgi", 200, "$")
        self.assertEqual(str(self.account), message)

    def test_negative_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-50)

    def test_positive_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 250)

    def test_bank_statement(self):
        self.account.balance += 1000
        self.assertEqual(self.account.bank_statement(), 1200)

    def test_withdraw_bigger_amount(self):
        self.assertFalse(self.account.withdraw(400), False)

    def test_withdraw_smaller_amount(self):
        self.assertTrue(self.account.withdraw(100), True)
        self.assertEqual(self.account.balance, 100)

    def test_history(self):
        self.assertEqual(self.account.operations, ["Account was created"])

    def test_transfer_to_wrong_currency(self):
        self.other_account = BankAccount("Zdravko", 1000, "BGN")
        with self.assertRaises(ValueError):
            self.account.transfer_to(self.other_account, 200)

    def test_transfer_to_bigger_amount(self):
        self.other_account = BankAccount("Pesho", 2000, "$")
        with self.assertRaises(ValueError):
            self.account.transfer_to(self.other_account, 500)

    def test_transfer_to(self):
        self.other_account = BankAccount("Kiro", 2500, "$")
        self.assertEqual(self.account.transfer_to(self.other_account, 1), True)
        self.assertEqual(self.account.balance, 199)
        self.assertEqual(self.other_account.balance, 2501)

if __name__ == '__main__':
    unittest.main()
