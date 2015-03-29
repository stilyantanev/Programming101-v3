class Bill:

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        # return str(self.amount)
        return "A {}$ bill".format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return int(self.amount)

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.amount)

# a = Bill(10)
# b = Bill(5)
# c = Bill(10)

# print(int(a))  # 10
# print(str(a))  # "A 10$ bill"
# print(a)  # A 10$ bill

# print(a == b)  # False
# print(a == c)  # True

# money_holder = {}

# money_holder[a] = 1  # We have one 10$ bill

# if c in money_holder:
#     money_holder[c] += 1

# print(money_holder)  # { "A 10$ bill": 2 }


class BatchBill():

    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        return len(self.bills)

    def __getitem__(self, index):
        return self.bills[index]

    def total(self):
        total_sum = 0

        for bill in self.bills:
            total_sum += int(bill)

        return total_sum

# values = [10, 20, 50, 100]
# bills = [Bill(value) for value in values]

# batch = BatchBill(bills)

# for bill in batch:
#     print(bill)

# A 10$ bill
# A 20$ bill
# A 50$ bill
# A 100$ bill


class CashDesk():

    def __init__(self):
        self.all_bills = []

    def take_money(self, money):
        self.all_bills.append(money)

    def total(self):
        result = 0
        for bill in self.all_bills:
            if isinstance(bill, Bill):
                result += int(bill)
            elif isinstance(bill, BatchBill):
                for single_bill in bill:
                    result += int(single_bill)

        return result

    def inspect(self):
        inspection = {}

        for bill in self.all_bills:
            if isinstance(bill, Bill):
                if bill in inspection:
                    inspection[bill] += 1
                elif bill not in inspection:
                    inspection[bill] = 1
            elif isinstance(bill, BatchBill):
                for single_bill in bill:
                    if single_bill in inspection:
                        inspection[single_bill] += 1
                    elif single_bill not in inspection:
                        inspection[single_bill] = 1

        return inspection

# values = [10, 20, 50, 100, 100, 100]
# bills = [Bill(value) for value in values]

# batch = BatchBill(bills)

# desk = CashDesk()

# desk.take_money(batch)
# desk.take_money(Bill(10))

# print(desk.total())  # 390
# print(desk.inspect())

# We have a total of 390$ in the desk
# We have the following count of bills, sorted in ascending order:
# 10$ bills - 2
# 20$ bills - 1
# 50$ bills - 1
# 100$ bills - 3
