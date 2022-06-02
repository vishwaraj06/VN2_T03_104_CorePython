# list=[1,2,3,4,5,6]
# for i in list:
#     print(i)

list=[9,8,7,6,5,4]
list=iter(list)#it creates iterators in the object which contains values
print(next(list))#get the values on the iterable objects(method1)
print(list.__next__())#method 2


