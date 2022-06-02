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
class raja:
    def company_info(self, company_name, location):
        print('Inside Company class')
        print('Name:', company_name, 'location:', location)

# Child class
class Employee(Person, Company,raja):
    def Employee_info(self, salary, skill):
        print('Inside Employee class')
        print('Salary:', salary, 'Skill:', skill)

emp = Employee()
# access data
emp.person_info('Raja', 28)
emp.company_info('CTS', 'Salem')
emp.Employee_info(13000, 'big data')
emp.company_info("chai","hydrabad")

print("###############################################################")
#Multilevel inheritance:
# Base class
class Vehicle:
    def Vehicle_info(self):
        print('TVS')
# Child class
class Car(Vehicle):
    def car_info(self):
        print('HONDA')
# Child class
class SportsCar(Car):
    def sports_car_info(self):
        print('Ferrari')
s_car = SportsCar()
s_car.Vehicle_info()
s_car.car_info()
s_car.sports_car_info()
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#Hierarchical inheritance
class Vehicle:
    def info(self):
        print("This is Vehicle")
class Car(Vehicle):
    def car_info(self, name):
        print("Car name is:", name)
class Truck(Vehicle):
    def truck_info(self, name):
        print("Truck name is:", name)
obj1 = Car()
obj1.info()
obj1.car_info('BMW')

obj2 = Truck()
obj2.info()
obj2.truck_info('Ford')
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#Hybrid inheritance
class Vehicle:
    def vehicle_info(self):
        print("Inside Vehicle class")
class Car(Vehicle):
    def car_info(self):
        print("Inside Car class")
class Truck(Vehicle):
    def truck_info(self):
        print("Inside Truck class")
# Sports Car can inherits properties of Vehicle and Car
class SportsCar(Car, Vehicle):
    def sports_car_info(self):
        print("Inside SportsCar class")

# create object
s_car = SportsCar()
s_car.vehicle_info()
s_car.car_info()
s_car.sports_car_info()