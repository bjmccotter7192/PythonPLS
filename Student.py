students = []


class Student:

    school_name = "Pocomoke Elementary"

    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_capitalize_name(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

Mark = Student("Mark")
print(Mark)

print(Student.school_name)
