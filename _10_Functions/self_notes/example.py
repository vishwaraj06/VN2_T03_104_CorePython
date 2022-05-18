'''def simple_interest(p,t,r):
    return (p*t*r)/100
p = float(input("Enter the principle amount?: "))
r = float(input("Enter the rate of interest? :"))
t = float(input("Enter the time in years? :"))
print("Simple Interest: ",simple_interest(p,r,t))


A = P(1 + R/100) t

 ci = p * (pow((1 + r / 100), t)) 
    return ci
def compund_interest(p,t,r):
    compund_interest=p*(pow((1+r/100),t))
    return compund_interest
p = float(input("Enter the principle amount?: "))
r = float(input("Enter the rate of interest? :"))
t = float(input("Enter the time in years? :"))
print("Compound interest:",compund_interest(p,r,t))
'''
class students():
    name="Tharun"
    age=28
    gender='male'

print(getattr(students,'name'))
print(students.name)
print(getattr(students,'age'))
print(getattr(students,'gender'))
students.city='salem'
print(students,'city')
print(students.__dict__)
print(getattr(students,'city'))
students.department='biology'
print(students.department)
print(students.__dict__)
del students.age
print(students.__dict__)
students.age=12
print(students.age)
print(type(students))



