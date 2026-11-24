class Student:
    def __init__(self, studentID, name, surname, age, department):
        self.studentID = studentID
        self.name = name
        self.surname = surname
        self.age = age
        self.department = department

    def getInfo(self):
        return f"{self.name} {self.surname} - {self.department}"

    def study(self):
        print(f"{self.name} is Active Student.")


student1 = Student(1001, "Mehmet", "Şahin", 22, "CIS")

print(student1.getInfo())
student1.study()