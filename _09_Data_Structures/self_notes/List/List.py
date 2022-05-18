mylist=[12,34,67,23,65,12,98]
print("List:",mylist)
#1 Append
mylist.append(999)
print(mylist)
print("$$$$$$$$$")
#2.copy
list2=mylist.copy()
print(list2)
print("$$$$$$$$$")
#3.extend
mylist.extend(list2)
print(mylist)
print("$$$$$$$$$")
#4.remove
mylist.remove(12)
print(mylist)
print("$$$$$$$$$")
#5 pop
mylist.pop(6)
print("after pop:",mylist)
print("$$$$$$$$$")
#6.reverse
mylist.reverse()
print("reversal list:",mylist)
print("$$$$$$$$$")
#7.sort
mylist.sort()
print("after sorting:",mylist)
print("$$$$$$$$$")
#accessing list
print("mylist[4]:",mylist[4])
print("mylist[4:9]",mylist[4:9])
#update list
mylist[2]=('raja')
print("after update:",mylist)
# delete list
del mylist[3]
print("after deleting index postion 3:",mylist)
#max
print("max of list:",max(list2))
#min
print("min of list:",min(list2))
#length
print("length of list:",len(mylist))

'''if ob2==1:
    print("Leap Year")
else:
    print("Not a Leap Year")'''

