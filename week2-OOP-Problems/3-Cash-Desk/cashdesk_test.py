import unittest
from cashdesk import Bill
from cashdesk import BatchBill
from cashdesk import CashDesk


class BillTest(unittest.TestCase):

    def setUp(self):
        self.bill = Bill(10)

    def test_create_new_bill_instance(self):
        self.assertTrue(isinstance(self.bill, Bill))

    def test_valid_member(self):
        self.assertEqual(self.bill.amount, 10)

    def test_str_casting(self):
        message = "A {}$ bill".format(self.bill.amount)
        self.assertEqual(str(self.bill), message)

    def test_repr_casting(self):
        message = "A {}$ bill".format(self.bill.amount)
        self.assertEqual(repr(self.bill), message)

    def test_int_casting(self):
        self.assertEqual(int(self.bill), 10)

    def test_equal_function(self):
        self.another_bill = Bill(10)
        self.assertEqual(self.bill.amount, self.another_bill.amount)

    def test_hash_function(self):
        self.assertTrue(isinstance(hash(self.bill.amount), int))


class BatchBillTest(unittest.TestCase):

    def setUp(self):
        self.batch = BatchBill(Bill(10))
        self.other_batch = BatchBill([Bill(10), Bill(20), Bill(30)])

    def test_new_batchbill_instance(self):
        self.assertTrue(isinstance(self.batch, BatchBill))

    def test_valid_member(self):
        self.assertEqual(self.batch.bills, Bill(10))

    def test_len_function(self):
        self.assertEqual(len(self.other_batch), 3)

    def test_getitem_function(self):
        self.assertEqual(self.other_batch[2], Bill(30))

    def test_total_function(self):
        total_cash = sum([int(bill)for bill in self.other_batch])
        self.assertEqual(self.other_batch.total(), total_cash)


class CashDeskTest(unittest.TestCase):

    def setUp(self):
        self.desk = CashDesk()

    def test_create_new_cashdesk_instance(self):
        self.assertTrue(isinstance(self.desk, CashDesk))

    def test_valid_member(self):
        self.assertEqual(self.desk.money_holder, {})

    def test_total_function(self):
        self.desk.take_money(Bill(10))
        self.desk.take_money(BatchBill([Bill(10), Bill(100), Bill(2000)]))
        self.assertEqual(self.desk.total(), 2120)

    def test_inspect_function(self):
        self.desk.take_money(Bill(10))
        self.desk.take_money(BatchBill([Bill(10), Bill(100), Bill(2000)]))
        result = {
            Bill(10): 2,
            Bill(100): 1,
            Bill(2000): 1,
        }
        self.assertEqual(self.desk.inspect(), result)


if __name__ == '__main__':
    unittest.main()
