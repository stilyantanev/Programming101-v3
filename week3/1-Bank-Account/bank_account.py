class BankAccount:

    def __init__(self, name, balance, currency):
        self.name = name
        self.balance = balance
        self.currency = currency
        self.operations = ["Account was created"]

    def __int__(self):
        message = "__int__ check -> {}{}"
        self.operations.append(message.format(self.balance, self.currency))

        return self.balance

    def __str__(self):
        message = "Bank account for {} with balance of {}{}"

        return message.format(self.name, self.balance, self.currency)

    def deposit(self, amount):
        if amount < 0:
            raise ValueError
        else:
            self.balance += amount
            message = "Deposited {}{}"
            self.operations.append(message.format(amount, self.currency))

    def bank_statement(self):
        message = "Balance check -> {}"
        self.operations.append(message.format(self.balance, self.currency))

        return self.balance

    def withdraw(self, amount):
        if self.balance < amount:
            message = "Withdraw for {}{} failed."
            self.operations.append(message.format(amount, self.currency))

            return False
        else:
            self.balance -= amount
            message = "{}{} was withdrawed"
            self.operations.append(message.format(amount, self.currency))

            return True

    def history(self):
        return self.operations

    def transfer_to(self, account, amount):
        if self.currency != account.currency:
            raise ValueError

        if self.balance < amount:
            raise ValueError

        self.balance -= amount
        account.balance += amount

        sender_message = "Transfer to {} for {}{}"
        sender = self.name
        receiver_message = "Transfer from {} for {}{}"
        receiver = account.name

        self.operations.append(
            sender_message.format(receiver, amount, self.currency))
        account.operations.append(
            receiver_message.format(sender, amount, account.currency))

        return True
