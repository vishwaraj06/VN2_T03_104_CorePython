#we can use looping(for) and condition(if condition) in list,the operation we are performing in list are called list comprehension
lst=[1,2,3,4,5,6]
# lst2=[]
# for i in lst:
#     square=i**2
#     lst2.append(square)
# print(lst2)

l_square=[square**2 for square in lst if square%2==0]
print(l_square)