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
        total_sum = 0

        for bill in self.bills:
            total_sum += int(bill)

        return total_sum


class CashDesk:

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
