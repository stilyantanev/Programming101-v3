class CommandIO:

    @staticmethod
    def prepare_company_database(company):
        company.establish_connection()
        company.create_table_employees()
        company.fill_database_with_data()
        print("Connection was established!")
        print("Company database was filled with data!")

    @staticmethod
    def list_employees(company):
        print(company.view_employees())

    @staticmethod
    def monthly_spending(company):
        spending = company.spending_for_month()
        print("The company is spending {}$ every month!".format(spending))

    @staticmethod
    def yearly_spending(company):
        spending = company.spending_for_year()
        print("The company is spending {}$ every year!".format(spending))

    @staticmethod
    def add(company):
        name = input("name>")
        salary = input("monthly_salary>")
        bonus = input("yearly_bonus>")
        position = input("position>")
        company.add_employee(name, salary, bonus, position)

    @staticmethod
    def delete(company, employee_id):
        company.delete_employee(employee_id)

    @staticmethod
    def update(company, employee_id):
        name = input("name>")
        salary = input("monthly_salary>")
        bonus = input("yearly_bonus>")
        position = input("position>")
        company.update_employee(name, salary, bonus, position, employee_id)

    @staticmethod
    def quit(company):
        company.close_connection()
        print("Connection was closed! Goodbye!")

    @staticmethod
    def command_parser(command):
        commands = command.split()

        return tuple(commands)

    @staticmethod
    def command_choice(company, command, employee_id=0):
        if command == "list_employees":
            CommandIO.list_employees(company)
        elif command == "monthly_spending":
            CommandIO.monthly_spending(company)
        elif command == "yearly_spending":
            CommandIO.yearly_spending(company)
        elif command == "add_employee":
            CommandIO.add(company)
        elif command == "delete_employee":
            CommandIO.delete(company, employee_id)
        elif command == "update_employee":
            CommandIO.update(company, employee_id)
        elif command == "quit":
            CommandIO.quit(company)
        else:
            print("Wrong choice! Please try again!")
