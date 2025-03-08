#Task 1 - Write a program to create a "Students" class, initialize attributes and create and print two instances of Students

class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f'{self.name} is {self.age} years old and currently in {self.grade} grade'

raj = Students("Raj", 16, "11th")
joe = Students("Joe", 17, "11th")

for student in [raj, joe]:
    print(student)

#Task 2 - Write a program to create a child class "Teacher" that inherits properties of its parent class "Staff"
class Staff:
    def __init__(self, name, department, role, salary):
        self.name = name
        self.department = department
        self.role = role
        self.salary = salary

class Teacher(Staff):
    def __init__(self, name, department, role, salary, age):
        super().__init__(name, department, role, salary)
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old and is a {self.role} in the {self.department} department making ${self.salary} per year'

raj = Teacher("Raj", "Science", "Teacher", 60000, 20)
joe = Teacher("Joe", "Science", "Teacher", 85000, 58)

for staff in [raj, joe]:
    print(staff)

#Task 3 - Write a Python class "Square" and define two methods that return the square area and perimeter given the length of a side
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

    def __str__(self):
        return f"A square with side length {self.side} has an area of {self.area()} and perimeter of {self.perimeter()}"

square1 = Square(7)
square2 = Square(2)
print(square1)
print(square2)