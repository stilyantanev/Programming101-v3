from bank_account import BankAccount


def main():
    account = BankAccount("Rado", 0, "$")
    print(account)
    account.deposit(1000)
    print(account.bank_statement())
    print(str(account))
    print(int(account))
    print(account.history())
    print(account.withdraw(500))
    print(account.bank_statement())
    print(account.history())
    print(account.withdraw(1000))
    print(account.bank_statement())
    print(account.history())

    rado = BankAccount("Rado", 1000, "BGN")
    ivo = BankAccount("Ivo", 0, "BGN")
    print(rado.transfer_to(ivo, 500))
    print(rado.bank_statement())
    print(ivo.bank_statement())
    print(rado.history())
    print(ivo.history())

if __name__ == '__main__':
    main()
