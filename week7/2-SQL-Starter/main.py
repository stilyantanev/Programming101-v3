from company import Company
from command_io import CommandIO


def main():

    company_database = Company("company.db")
    CommandIO.prepare_company_database(company_database)

    command = ""
    while command != "quit":
        command = input("command>")
        commands = CommandIO.command_parser(command)
        CommandIO.command_choice(company_database, *commands)

if __name__ == '__main__':
    main()
