'''

tup1=(1,2,3,4,5,6,7,8,9,10)
set1={1,2,3,4,5,6,7,8,9,10}
result1=list(map(lambda x:x*x,list1))
result2=list(map(lambda x:x*x,tup1))
result3=list(map(lambda x:x*x,set1))
print("add",result1)
print("add",result2)
print("add",result3)
def mul(list1):
     s=0
     for i in list1:
         s=s*list1
     return s
print("Multiplication of list:",mul(list1))'''
def mul(num):
    total=1
    for i in num:
        total=total*i
    return total
print("Multiplication of list:",mul(num=[1,2,3,4,5,6]))


def mul(num):
    total=1
    for i in num:
        total=total*i
    return total
print("Multiplication of Tuples:",mul(num=(1,2,3,4,5,6)))


def mul(num):
    total=1
    for i in num:
        total=total*i
    return total
print("Multiplication of Set:",mul(num={1,2,3,4,5,6}))
