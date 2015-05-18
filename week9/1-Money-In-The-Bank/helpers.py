from hashlib import sha1
from settings import SALT

from uuid import uuid4

import smtplib
from my_email_password import MY_EMAIL, MY_PASSWORD


def send_email(email, message):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(MY_EMAIL, MY_PASSWORD)
    server.sendmail(MY_EMAIL, email, message)
    server.quit()


def hash_password(password):
    hashed_password = sha1()
    hashed_password.update((password + SALT).encode("utf8"))

    return hashed_password.hexdigest()


def password_validator(username, password):
    '''Password must have least 2 lower case letters, 2 upper case letters,
       2 digits, 2 symbols.
    '''

    is_password_valid = False

    MIN_LENGTH_OF_PASSWORD = 8
    MIN_SYMBOLS_BY_TYPE = 2

    LOWER_CASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
    UPPER_CASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    DIGITS = "0123456789"
    SYMBOLS = "!\"#$%&'()*+,-./:;<=>?@[\]^`{}|~"

    lower_case_letters = 0
    upper_case_letters = 0
    digits = 0
    symbols = 0

    for char in password:
        if char in LOWER_CASE_LETTERS:
            lower_case_letters += 1
        if char in UPPER_CASE_LETTERS:
            upper_case_letters += 1
        if char in DIGITS:
            digits += 1
        if char in SYMBOLS:
            symbols += 1

    is_not_password_in_username = password not in username
    is_not_username_in_password = username not in password
    is_password_more_than_8_symbols = len(password) >= MIN_LENGTH_OF_PASSWORD

    if lower_case_letters >= MIN_SYMBOLS_BY_TYPE and \
       upper_case_letters >= MIN_SYMBOLS_BY_TYPE and \
       digits >= MIN_SYMBOLS_BY_TYPE and \
       symbols >= MIN_SYMBOLS_BY_TYPE and \
       is_not_password_in_username and \
       is_not_username_in_password and \
       is_password_more_than_8_symbols:

            is_password_valid = True

    return is_password_valid


def generate_tan_codes(number):
    codes = []

    for i in range(number):
        codes.append(str(uuid4()).replace('-', ''))

    return codes
