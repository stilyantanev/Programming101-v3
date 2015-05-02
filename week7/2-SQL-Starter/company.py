import sqlite3


class Company:

    MONTHS = 12

    def __init__(self, database):
        self.database = database
        self.connection = None
        self.cursor = None

    def establish_connection(self):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.connection.close()

    def create_table_employees(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS employees(
            id INTEGER PRIMARY KEY,
            name TEXT,
            monthly_salary INTEGER,
            yearly_bonus INTEGER,
            position TEXT)
        """

        self.cursor.execute(create_table_query)
        self.connection.commit()

    def fill_database_with_data(self):
        insert_employees_query = """
        INSERT INTO employees(
            name,
            monthly_salary,
            yearly_bonus,
            position)
        VALUES(?,?,?,?)
        """

        employees = [("Ivan Ivanov", 5000, 10000, "Software Developer"),
                     ("Rado Rado", 500, 0, "Technical Support Intern"),
                     ("Ivo Ivo", 10000, 100000, "CEO"),
                     ("Petar Petrov", 3000, 1000, "Marketing Manager"),
                     ("Maria Georgieva", 8000, 10000, "COO")]

        self.cursor.executemany(insert_employees_query, employees)
        self.connection.commit()

    def view_employees(self):
        view_employees_query = """
            SELECT id, name, position FROM employees
            """

        self.cursor.execute(view_employees_query)
        all_rows = self.cursor.fetchall()

        all_employees = []
        for row in all_rows:
            employee = "{0} - {1} - {2}".format(row[0], row[1], row[2])
            all_employees.append(employee)
        all_employees = "\n".join(all_employees)

        return all_employees

    def spending_for_month(self):
        spending_for_month_query = """
            SELECT SUM(monthly_salary) FROM employees
            """

        self.cursor.execute(spending_for_month_query)
        salaries = self.cursor.fetchone()[0]

        return salaries

    def spending_for_year(self):
        spending_for_year_query = """
            SELECT SUM(monthly_salary), SUM(yearly_bonus) FROM employees
            """

        self.cursor.execute(spending_for_year_query)
        salaries = self.cursor.fetchall()[0]
        salaries = salaries[0] * self.MONTHS + salaries[1]

        return salaries

    def add_employee(self, name, salary, bonus, position):
        add_employee_query = """
            INSERT INTO employees(
                name,
                monthly_salary,
                yearly_bonus,
                position)
            VALUES(?, ?, ?, ?)
            """

        employee_parameters = (name, salary, bonus, position)
        self.cursor.execute(add_employee_query, employee_parameters)
        self.connection.commit()

    def delete_employee(self, employee_id):
        delete_employee_query = """
            DELETE FROM employees WHERE id = ?
        """

        self.cursor.execute(delete_employee_query, employee_id)
        self.connection.commit()

    def update_employee(self, name, salary, bonus, position, employee_id):
        update_employee_query = """
            UPDATE employees SET
                name = ?,
                monthly_salary = ?,
                yearly_bonus = ?,
                position = ?
            WHERE id = ?
        """

        employee_parameters = (name, salary, bonus, position, employee_id)
        self.cursor.execute(update_employee_query, employee_parameters)
        self.connection.commit()
