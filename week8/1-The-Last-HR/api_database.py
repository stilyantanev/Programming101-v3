import sqlite3


class Database:

    def __init__(self, database):
        self.database = database
        self.connection = None
        self.cursor = None

    def establish_connection(self):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.connection.close()

    def make_tables(self):
        self.create_table_students()
        self.create_table_courses()
        self.create_junction_table()

    def create_table_students(self):
        create_table_students_query = """
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY,
            name TEXT,
            github TEXT
        )
        """

        self.cursor.execute(create_table_students_query)
        self.connection.commit()

    def create_table_courses(self):
        create_table_courses_query = """
        CREATE TABLE IF NOT EXISTS courses(
            id INTEGER PRIMARY KEY,
            name TEXT
        )
        """

        self.cursor.execute(create_table_courses_query)
        self.connection.commit()

    def create_junction_table(self):
        create_junction_query = """
        CREATE TABLE IF NOT EXISTS students_to_courses(
            student_id INTEGER,
            course_id INTEGER,
            PRIMARY KEY(student_id, course_id),
            FOREIGN KEY (student_id) REFERENCES students(id),
            FOREIGN KEY (course_id) REFERENCES courses(id)
        )
        """

        self.cursor.execute(create_junction_query)
        self.connection.commit()

    def fill_courses_table(self, courses):
        insert_courses_query = """
        INSERT INTO courses(
            name)
        VALUES(?)
        """

        self.delete_courses_table()

        self.cursor.executemany(insert_courses_query, courses)
        self.connection.commit()

    def delete_courses_table(self):
        delete_courses_query = """
        DELETE FROM courses
        """
        self.cursor.execute(delete_courses_query)
        self.connection.commit()

    def fill_students_table(self, students):
        insert_students_query = """
        INSERT INTO students(
            name,
            github)
        VALUES(?, ?)
        """

        self.delete_students_table()
        self.cursor.executemany(insert_students_query, students)
        self.connection.commit()

    def delete_students_table(self):
        delete_students_query = """
        DELETE FROM students
        """

        self.cursor.execute(delete_students_query)
        self.connection.commit()

    def fill_junction_table(self, students_and_courses):
        insert_junction_query = """
        INSERT INTO students_to_courses(
            student_id,
            course_id)
        VALUES(?, ?)
        """

        course_id_query = """
        SELECT id FROM courses WHERE name = ?
        """

        junction_table_info = []
        for student_and_course in students_and_courses:
            student_id = student_and_course[0]
            courses_names = student_and_course[1]

            for course_name in courses_names:
                self.cursor.execute(course_id_query, (course_name,))
                course_id = self.cursor.fetchone()
                junction_table_info.append((student_id, course_id[0]))

        self.delete_junction_table()
        self.cursor.executemany(insert_junction_query, junction_table_info)
        self.connection.commit()

    def delete_junction_table(self):
        delete_junction_query = """
        DELETE FROM students_to_courses
        """

        self.cursor.execute(delete_junction_query)
        self.connection.commit()

    def view_students(self):
        view_students_query = """
        SELECT id, name, github FROM students
        """

        self.cursor.execute(view_students_query)
        records = self.cursor.fetchall()

        all_students = []
        for record in records:
            student = "{} -- {} -- {}".format(record[0], record[1], record[2])
            all_students.append(student)
        all_students = "\n".join(all_students)

        return all_students

    def view_courses(self):
        view_courses_query = """
        SELECT id, name FROM courses
        """

        self.cursor.execute(view_courses_query)
        records = self.cursor.fetchall()

        all_courses = []
        for record in records:
            course = "{} -- {}".format(record[0], record[1])
            all_courses.append(course)
        all_courses = "\n".join(all_courses)

        return all_courses

    def view_student_and_courses(self):
        view_student_and_courses_query = """
        SELECT students.name, courses.name
        FROM courses JOIN students
        ON courses.id IN (
            SELECT course_id
            FROM students_to_courses
            WHERE student_id = students.id)
        """

        self.cursor.execute(view_student_and_courses_query)
        records = self.cursor.fetchall()

        all_students_and_courses = []
        for record in records:
            student_and_course = "{} --- {}".format(record[0], record[1])
            all_students_and_courses.append(student_and_course)
        all_students_and_courses = "\n".join(all_students_and_courses)

        return all_students_and_courses

    def view_most_active_student(self):
        view_most_active_students_query = """
        SELECT students.name, COUNT(students_to_courses.student_id)
        FROM students JOIN students_to_courses
        ON students.id = student_id
        WHERE students.id IN (
            SELECT student_id
            FROM students_to_courses
            GROUP BY student_id
            ORDER BY COUNT(*) DESC
            LIMIT 1)
        """

        self.cursor.execute(view_most_active_students_query)
        records = self.cursor.fetchall()

        most_active_student = []
        for record in records:
            message = "{} participate in {} courses!"
            active_student = message.format(record[0], record[1])
            most_active_student.append(active_student)
        most_active_student = "\n".join(most_active_student)

        return most_active_student
