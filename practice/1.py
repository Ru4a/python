class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("학생 이름 : ",self.name)
        print("나이 : ",self.age)

student1 = Student('Albert', 30)

student1.display_info()