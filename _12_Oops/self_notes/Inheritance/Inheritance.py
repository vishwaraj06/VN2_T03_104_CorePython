#single inheritance
class Vehicle:
    def Vehicle_info(self):
        print('Inside Vehicle class')
# Child class
class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')
car = Car()
car.Vehicle_info()
car.car_info()

print("********************************************")

#Multiple Inheritance
# Parent class 1
class Person:
    def person_info(self, name, age):
        print('Inside Person class')
        print('Name:', name, 'Age:', age)
# Parent class 2
class Company:
    def company_info(self, company_name, location):
        print('Inside Company class')
        print('Name:', company_name, 'location:', location)
# Child class
class Employee(Person, Company):
    def Employee_info(self, salary, skill):
        print('Inside Employee class')
        print('Salary:', salary, 'Skill:', skill)

emp = Employee()
# access data
emp.person_info('Raja', 28)
emp.company_info('CTS', 'Salem')
emp.Employee_info(13000, 'big data')

print("###############################################################")
#Multilevel inheritance:
