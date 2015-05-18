from getpass import getpass


class View:

    def __init__(self, controller):
        self.controller = controller

    def input_username(self):
        '''Checking for existing on same user,
           if exist prompt for new input,
           if not exist return the new username.'''

        is_user_with_same_name = True
        while is_user_with_same_name:
            username = input("Enter username> ")

            is_user_with_same_name = self.controller.check_username(username)

            if is_user_with_same_name:
                print("There is registered user with same name!")
                print("Try with another name!")

        return username

    def input_registered_username(self):
        '''Checking for exist same user,
           if exist return username,
           if not exist prompt for new input.'''

        is_username_exists = False
        while not is_username_exists:
            username = input("Enter username> ")
            is_username_exists = self.controller.check_username(username)

            if not is_username_exists:
                print("Such username don't exist in the system!")
                print("Try with another one!")

        return username

    def input_email(self):
        '''Checking for existing on same email,
           if exist prompt for new input,
           if not exist return the new email.'''

        is_user_with_same_email = True
        while is_user_with_same_email:
            email = input("Enter email> ")

            is_user_with_same_email = self.controller.check_email(email)
            if is_user_with_same_email:
                print("There is registered user with same email!")
                print("Try with another email!")

        return email

    def input_valid_password(self, username):
        '''Get username and input for password,
           then check them are valid,
           when they get valid return password.'''

        is_valid_pass = False

        while not is_valid_pass:
            password = getpass(prompt="Enter password> ")
            is_valid_pass = self.controller.check_password(username, password)

            if not is_valid_pass:
                print("Password must have least:")
                print("2 lower case letters,")
                print("2 upper case letters,")
                print("2 digits,")
                print("2 symbols")

        return password

    def register(self):
        '''Register given user in system.'''

        username = self.input_username()
        email = self.input_email()
        password = self.input_valid_password(username)

        self.controller.register(username, password, email)

        print("Registered succesfully! Congratulations!")

    def validate_login(self):
        '''Validate all information about login.'''

        user = self.input_registered_username()

        is_logged = False

        while not is_logged:
            password = self.input_valid_password(user)
            is_logged = self.controller.login(user, password)

            if not is_logged:
                print("Wrong password!")
                print("Try again!")

        return user

    def login(self):
        '''Login given user in system. Return user.'''

        username = self.validate_login()
        print("You succesfully logged!")

        self.input_command_logged_menu(username)

    def input_command_main_menu(self):
        command = ""
        while command != "exit":
            command = input("$$$> ")
            self.command_choice_main_menu(command)

    def command_choice_main_menu(self, command):
        if command == "register":
            self.register()
        elif command == "login":
            self.login()
        elif command == "help":
            self.help_main_menu()
        elif command == "exit":
            self.exit_main_menu()
        else:
            print("Wrong choice! Please try again!")

    def input_command_logged_menu(self, user):
        command = ""
        while command != "exit":
            command = input("Logged> ")
            self.command_choice_logged_menu(command, user)

    def command_choice_logged_menu(self, command, username):
        if command == "account-info":
            self.print_account_info(username)
        elif command == "change-password":
            self.change_password(username)
        elif command == "change-email":
            self.change_email(username)
        elif command == "get-tan-codes":
            self.make_tans(username)
        elif command == "deposit":
            self.make_deposit(username)
        elif command == "withdraw":
            self.make_withdraw(username)
        elif command == "help":
            self.help_logged_menu()
        elif command == "exit":
            self.exit_logged_menu()
        else:
            print("Wrong choice! Please try again!")

    def start_taking_commands(self):
        self.input_command_main_menu()

    def help_main_menu(self):
        print ("1. register")
        print("You must type 'username' and 'password' to register!")
        print ("2. login")
        print("You must type your 'username' and 'password' to login!")
        print ("3. help")
        print("This command will show you this menu!")
        print ("4. exit")
        print("You will exit our system! Be carefull!")

    def help_logged_menu(self):
        print ("1. account-info")
        print("Showing info about your account!")
        print ("2. change-password")
        print("Change password with new one!")
        print ("3. get-tan-codes")
        print("With this codes you can deposit or withdraw!")
        print ("4. deposit")
        print("You can put money into your account!")
        print ("5. withdraw")
        print("You can take money from your account!")
        print ("6. help")
        print("This command will show you this menu!")
        print ("7. exit")
        print("You will exit from your account! Be carefull!")

    def exit_main_menu(self):
        print("Bank system closed doors!")
        print("Goodbye!")

    def exit_logged_menu(self):
        print("You quited from your account!")
        print("Goodbye!")

    def make_withdraw(self, username):
        ammount = int(input("Enter ammount: "))
        tan_code = input("Enter TAN code: ")

        is_withdrawed = self.controller.withdraw(username, ammount, tan_code)

        if is_withdrawed is None:
            print("You don't have this money in account!")
        elif is_withdrawed:
            print("You already withdrawed {} !".format(ammount))
        else:
            print("Tan code already used!")

    def make_deposit(self, username):
        ammount = int(input("Enter ammount: "))
        tan_code = input("Enter TAN code: ")

        is_deposited = self.controller.deposit(username, ammount, tan_code)

        if is_deposited:
            print("You already deposited {} !".format(ammount))
        else:
            print("Your TAN code is used!")

    def make_tans(self, username):
        is_send_tans = self.controller.make_tans(username)
        if is_send_tans:
            print("Tans sent to your email address!")
        elif not is_send_tans:
            print("You already have tans! Use it!")

    def change_password(self, username):
        password = getpass(prompt="Enter password> ")
        self.controller.change_password(username, password)
        print("Password was changed!")

    def print_account_info(self, user):
        username, email, balance = self.controller.get_account_info(user)
        print("You username is: {}".format(username))
        print("You email is: {}".format(email))
        print("You balance is: {}".format(balance))
