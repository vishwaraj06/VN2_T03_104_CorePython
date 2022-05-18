class Employee:
    def __init__(self,name,salary,project):
        self.name=name
        self.salary=salary
        self.project=project

    def show(self):
        print("Name:",self.name,"salary:",self.salary)

    def work(self):
        print(self.name,"is working on",self.project)
emp=Employee("Raja",12000,"NTT DATA")
emp.show()
emp.work()

#
class Employee:#public methods
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
       print("Name: ", self.name,"\n" 'Salary:', self.salary)

emp = Employee('Raja', 12000)
#print("Name: ", emp.name, 'Salary:', emp.salary)
emp.show()

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

emp = Employee('Raja', 20000)
print('Salary:', emp.__salary)#we can't access the private .
To access this we have two approaches
[1] create public methods to access the private  members
[2] name mangling for example(_Employee__salary)

# #1 create public methods to access the private  members
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    def show(self):
        # private members are accessible from a class
        print("Name: ", self.name, "\n"'Salary:', self.__salary)
emp = Employee('Raja', 20000)
emp.show()

print("***********************************************************")

# #2. Name mangling
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

emp = Employee('Tharun', 21000)
print('Name:', emp.name)
# direct access to private member using name mangling
print('Salary:', emp._Employee__salary)