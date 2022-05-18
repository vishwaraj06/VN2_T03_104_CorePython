tup1=(11,12,13,14,15,16,"raja",9.7,"anu")
print("Tuple:",tup1[4])
print("Tuple:",tup1[4:9])
tup2=(1,2,3,4,5,6,"gowri")
tup3=tup1+tup2
print("tuple 3:",tup3)  #Tuples are immutable which means you cannot update or change the values of tuple elements. You are able to take portions of existing tuples to create new tuples
#Removing individual tuple elements is not possible
#del tup1
print(tup1)
print(tup3)
print("*****************************************")
tup4=(11, 12, 13, 14, 15, 16, 'raja', 9.7, 'anu', 1, 2, 3, 4, 5, 6, 'gowri')
print("length of tuple:",len(tup4))
tup5=(99,98,97,96,95)
print("concatination:",tup4+tup5)
print("maximum:",max(tup5))
print("minimum:",min(tup5))
