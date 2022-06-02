class Company:
    def company_name(self):
        return 'VN2'

class Employee(Company):
    def info(self):
        # Calling the superclass method using super()function
        cname = super().company_name()
        print("Raja works at", cname)

# Creating object of child class
emp = Employee()
emp.info()