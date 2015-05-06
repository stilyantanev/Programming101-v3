class Handler:

    def __init__(self, data):
        self.data = data
        self.students = self.students_information()
        self.courses = self.courses_information()
        self.students_and_courses = self.students_and_courses_info()

    def get_data(self):
        return self.data

    def students_information(self):
        student_info = []

        for student in self.data:
            name = student["name"]
            github = student["github"]
            student_info.append((name, github))

        return student_info

    def courses_information(self):
        courses_info = set()

        for i in range(0, len(self.data)):
            courses = self.data[i]["courses"]

            for course in courses:
                courses_info.add((course["name"],))

        return list(courses_info)

    def students_and_courses_info(self):
        students_and_courses_info = []

        for i in range(0, len(self.data)):
            id_number = i + 1
            courses = []
            for course in self.data[i]["courses"]:
                courses.append(course["name"])
            students_and_courses_info.append((id_number, courses))

        return students_and_courses_info
