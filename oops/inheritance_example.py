# IS A RELATIONSHIP
# STUDENT(college, year, degree) IS A PERSON(name, address)

class Person:
    def __init__(self, name, address = 'NA'):
        self.name = name
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Address: {self.address}"

class Student(Person):
    def __init__(self, name, address, college, year, degree):
        super().__init__(name, address)
        self.college = college
        self.year = year
        self.degree = degree

    def __str__(self):
        return super().__str__() + f", College: {self.college}, Year: {self.year}, Degree: {self.degree}"

person1 = Person('Arjun')
print(person1)

student1 = Student('Arjun B','Pune', 'Pune University', 2014, 'BE')
print(student1)

