class CommandIO:

    @staticmethod
    def show_menu():
        print("Welcome to our database with students! Enjoy!")
        print("Here are possible commands:")
        print("students information")
        print("courses information")
        print("student and courses")
        print("most active student")
        print("quit")

    @staticmethod
    def input_command(database):
        command = ""
        while command != "quit":
            command = input("command>")
            CommandIO.command_choice(database, command)

    @staticmethod
    def command_choice(database, command):
        if command == "students information":
            CommandIO.students_information(database)
        elif command == "courses information":
            CommandIO.courses_information(database)
        elif command == "student and courses":
            CommandIO.student_and_courses_information(database)
        elif command == "most active student":
            CommandIO.most_active_student_informtion(database)
        elif command == "quit":
            CommandIO.quit(database)
        else:
            print("Wrong choice! Please try again!")

    @staticmethod
    def student_and_courses_information(database):
        student_and_courses = database.view_student_and_courses()
        print(student_and_courses)

    @staticmethod
    def most_active_student_informtion(database):
        most_active_student = database.view_most_active_student()
        print(most_active_student)

    @staticmethod
    def courses_information(database):
        courses = database.view_courses()
        print(courses)

    @staticmethod
    def students_information(database):
        students = database.view_students()
        print(students)

    @staticmethod
    def quit(database):
        database.close_connection()
        print("Connection was closed! Goodbye!")
