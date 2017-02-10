class Bill:

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return int(self.amount)

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.amount)


class BatchBill:

    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        return len(self.bills)

    def __getitem__(self, index):
        return self.bills[index]

    def total(self):
        return sum([int(bill) for bill in self.bills])


class CashDesk:

    def __init__(self):
        self.money_holder = {}

    def __store_bill(self, bill):
        if bill not in self.money_holder:
            self.money_holder[bill] = 1
        else:
            self.money_holder[bill] += 1

    def take_money(self, money):
        if isinstance(money, Bill):
            self.__store_bill(money)
        elif isinstance(money, BatchBill):
            for bill in money:
                self.__store_bill(bill)

    def total(self):
        money_holder = self.money_holder
        return sum([int(bill) * money_holder[bill] for bill in money_holder])

    def inspect(self):
        total = self.total()
        print("\nWe have a total {}$ in the desk".format(total))

        info = ("We have the following count of bills, "
                "sorted in ascending order:")
        print(info)

        for bill in self.money_holder:
            print("{0} - {1}".format(bill, self.money_holder[bill]))

        return self.money_holder
