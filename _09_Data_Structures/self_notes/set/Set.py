s={1,2,3,4,'raja',4,8,9,2,4,3,23,(1,2,3)}
print("value of sets:",s,type(s),id(s))
for i in s:
    print(i)
print("*********************************")
s.add(404)
print("After update:",s) # update set
s.remove(23)
print("After removal:",s) # removal set items
s1={9,1,3,8,12,15}
print("Union of set:",s|s1)#union of set
print("intersection s-s1:",s-s1)#intersection
print("intersection s1-s:",s1-s)


