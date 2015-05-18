from sqlalchemy.orm import Session
from sqlalchemy.sql import exists
from sqlalchemy import create_engine
from sqlalchemy import and_
from base import Base

from helpers import password_validator
from helpers import hash_password
from helpers import generate_tan_codes
from helpers import send_email

from models import Client, TanCode


class Controller:

    def __init__(self, database_connection):
        self.engine = create_engine(database_connection)
        self.session = Session(bind=self.engine)

        Base.metadata.create_all(self.engine)

    def check_password(self, username, password):
        return password_validator(username, password)

    # REGISTER
    def check_username(self, username):
        is_username = self.session.query(
            exists().where(Client.username == username)).scalar()

        return is_username

    def check_email(self, email):
        is_email = self.session.query(
            exists().where(Client.email == email)).scalar()

        return is_email

    def register(self, username, password, email):
        client = Client(username=username,
                        email=email,
                        password=hash_password(password))

        self.session.add(client)
        self.session.commit()

    def login(self, username, password):
        new_pass = hash_password(password)
        is_name_and_pass = self.session.query(exists().where(
            and_(Client.username == username, Client.password == new_pass)))

        is_name_and_pass = is_name_and_pass.scalar()

        return is_name_and_pass

    def get_account_info(self, username):
        account = self.session.query(Client).filter(
            Client.username == username).one()

        return [account.username, account.email, account.balance]

    def change_password(self, username, password):
        account = self.session.query(Client).filter(
            Client.username == username).one()

        account.password = hash_password(password)
        self.session.commit()

    def make_tans(self, username):
        TAN_COUNT = 10

        account = self.session.query(Client).filter(
            Client.username == username).one()

        user_email = account.email

        is_tan_codes_for_user = self.session.query(
            exists().where(TanCode.client_id == account.id)).scalar()

        if not is_tan_codes_for_user:
            codes = generate_tan_codes(TAN_COUNT)
            for code in codes:
                new_code = TanCode(
                    tan_code=code, is_used=0, client_id=account.id)
                self.session.add(new_code)
            self.session.commit()

            message = "\n".join(codes)
            send_email(user_email, message)
            return True
        else:
            return False

    def deposit(self, username, ammount, tan_code):
        account = self.session.query(Client).filter(
            Client.username == username).one()

        tan_code = self.session.query(TanCode).filter(
            TanCode.tan_code == tan_code).one()

        if tan_code.is_used == 0:
            account.balance += ammount
            tan_code.is_used = 1
            self.session.commit()
            return True
        else:
            return False

    def withdraw(self, username, ammount, tan_code):
        account = self.session.query(Client).filter(
            Client.username == username).one()

        if account.balance < ammount:
            return None

        tan_code = self.session.query(TanCode).filter(
            TanCode.tan_code == tan_code).one()

        if tan_code.is_used == 0:
            account.balance -= ammount
            tan_code.is_used = 1
            self.session.commit()
            return True
        else:
            return False
