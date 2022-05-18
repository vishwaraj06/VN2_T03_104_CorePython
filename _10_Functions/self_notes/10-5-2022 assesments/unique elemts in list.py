def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    for x in unique_list:
      print(x)
list1 =['hai','hai','how',1,3,4,2,3,2,1]
print("the unique elements in the list is",)
unique(list1)


