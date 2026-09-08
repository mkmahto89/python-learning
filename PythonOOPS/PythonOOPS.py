"""
FULL PYTHON OOPS CONCEPT DEMO
Covers:
1. Class & Object
2. Constructor
3. Instance Variables
4. Class Variables
5. Instance Method
6. Class Method
7. Static Method
8. Encapsulation
9. Inheritance
10. Multilevel Inheritance
11. Multiple Inheritance
12. Polymorphism
13. Method Overriding
14. Abstraction
15. Operator Overloading
16. Property Decorators
17. Composition
18. Aggregation
19. Duck Typing
20. Magic Methods
"""

from abc import ABC, abstractmethod


# =========================================================
# 1. CLASS, OBJECT, CONSTRUCTOR
# =========================================================

class Person:
    # Class Variable
    country = "India"

    def __init__(self, name, age):
        # Instance Variables
        self.__name = name       # Encapsulation (Private)
        self.__age = age

    # Instance Method
    def display(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")

    # Getter
    def get_age(self):
        return self.__age

    # Setter
    def set_age(self, age):
        if age > 0:
            self.__age = age

    # Property Decorator
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    # Class Method
    @classmethod
    def change_country(cls, new_country):
        cls.country = new_country

    # Static Method
    @staticmethod
    def greet():
        print("Welcome to Python OOPS")


# =========================================================
# 2. INHERITANCE
# =========================================================

class Employee(Person):

    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def display_employee(self):
        self.display()
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.salary}")


# =========================================================
# 3. METHOD OVERRIDING + POLYMORPHISM
# =========================================================

class Animal:
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


# =========================================================
# 4. MULTILEVEL INHERITANCE
# =========================================================

class Grandfather:
    def house(self):
        print("Grandfather House")


class Father(Grandfather):
    def car(self):
        print("Father Car")


class Son(Father):
    def bike(self):
        print("Son Bike")


# =========================================================
# 5. MULTIPLE INHERITANCE
# =========================================================

class Mother:
    def skills(self):
        print("Cooking")


class Father2:
    def business(self):
        print("Business Skills")


class Child(Mother, Father2):
    pass


# =========================================================
# 6. ABSTRACTION
# =========================================================

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car Started")


# =========================================================
# 7. OPERATOR OVERLOADING
# =========================================================

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Magic Method
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def show(self):
        print(f"Point({self.x}, {self.y})")


# =========================================================
# 8. COMPOSITION has a relation ,strong
# =========================================================

class Engine:

    def start_engine(self):
        print("Engine Started")


class Car2:

    def __init__(self):
        self.engine = Engine()   # Composition

    def start_car(self):
        self.engine.start_engine()
        print("Car Started")


# =========================================================
# 9. AGGREGATION loose
# =========================================================

class Department:

    def __init__(self, dept_name):
        self.dept_name = dept_name


class College:

    def __init__(self, college_name, department):
        self.college_name = college_name
        self.department = department   # Aggregation


# =========================================================
# 10. DUCK TYPING
# =========================================================

class VSCode:
    def execute(self):
        print("Running code in VSCode")


class PyCharm:
    def execute(self):
        print("Running code in PyCharm")


class Laptop:

    def code(self, ide):
        ide.execute()


# =========================================================
# 11. MAGIC METHODS
# =========================================================

class Book:

    def __init__(self, pages):
        self.pages = pages

    def __str__(self):
        return f"Book with {self.pages} pages"

    def __len__(self):
        return self.pages


# =========================================================
# MAIN PROGRAM
# =========================================================

print("\n===== BASIC CLASS & OBJECT =====")
p1 = Person("Mohit", 22)
p1.display()

print("\n===== GETTER & SETTER =====")
print("Age:", p1.get_age())
p1.set_age(25)
print("Updated Age:", p1.get_age())

print("\n===== PROPERTY DECORATOR =====")
print("Name:", p1.name)
p1.name = "Rahul"
print("Updated Name:", p1.name)

print("\n===== CLASS METHOD =====")
print("Country:", Person.country)
Person.change_country("Canada")
print("Updated Country:", Person.country)

print("\n===== STATIC METHOD =====")
Person.greet()

print("\n===== INHERITANCE =====")
emp = Employee("Amit", 30, 101, 50000)
emp.display_employee()

print("\n===== POLYMORPHISM =====")
animals = [Dog(), Cat()]

for a in animals:
    a.sound()

print("\n===== MULTILEVEL INHERITANCE =====")
s = Son()
s.house()
s.car()
s.bike()

print("\n===== MULTIPLE INHERITANCE =====")
c = Child()
c.skills()
c.business()

print("\n===== ABSTRACTION =====")
car = Car()
car.start()

print("\n===== OPERATOR OVERLOADING =====")
p1 = Point(2, 3)
p2 = Point(4, 5)

p3 = p1 + p2
p3.show()

print("\n===== COMPOSITION =====")
car_obj = Car2()
car_obj.start_car()

print("\n===== AGGREGATION =====")
dept = Department("Computer Science")
college = College("ABC College", dept)

print("College:", college.college_name)
print("Department:", college.department.dept_name)

print("\n===== DUCK TYPING =====")
lap = Laptop()

vscode = VSCode()
pycharm = PyCharm()

lap.code(vscode)
lap.code(pycharm)

print("\n===== MAGIC METHODS =====")
b = Book(500)

print(b)
print("Length:", len(b))

# this function saying expected input is string and return type is INT but just warning no strict warning 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: