from api_crawler import Crawler
from api_information_handler import Handler
from api_database import Database
from api_command_io import CommandIO


def prepare_database():
    crawler = Crawler()
    data = crawler.get_data()

    information = Handler(data)

    database = Database("students.db")
    database.establish_connection()
    database.make_tables()

    courses = information.courses
    database.fill_courses_table(courses)

    students = information.students
    database.fill_students_table(students)

    students_and_courses = information.students_and_courses
    database.fill_junction_table(students_and_courses)

    return database


def main():

    database = prepare_database()
    CommandIO.show_menu()
    CommandIO.input_command(database)

if __name__ == '__main__':
    main()
