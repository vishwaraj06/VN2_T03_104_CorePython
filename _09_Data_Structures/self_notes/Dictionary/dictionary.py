dict1={'name':'raja','age':21,'gender':'male','destination':'Student'}
print(dict1)
print("Retrive:",dict1['name'])
print("Retrive:",dict1['name'],dict1['age'])
'''for key in dict1():
    print(key)
for values in dict1():
        print(values)'''
dict1['name']='Tharun'
print("after update:",dict1)
del dict1['age']
print("after deletion:",dict1)
print("****************************************")
dict2={'name':'raja','age':21,'gender':'male','destination':'Student','name':'Gowri'}
print("Duplicate key name :",dict2)# if we enter duplicate keys encountered during assignment, the last assignment wins
print("length of dictionary:",len(dict2))
print("string:",str(dict2)) #This method returns string representation.
dict3=dict2.copy()
print("dict3:",dict3)
print("********************************************")
seq = ('name', 'age', 'sex') # fromkeys() creates a new dictionary with keys from seq and values set to value.
dict = dict.fromkeys(seq)
print("dict4 :", str(dict))
seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq,6)
print("dict5:" ,str(dict))
#print("hash function:",dict3.__hash__('age'))#has_key() returns true if a given key is available in the dictionary, otherwise it returns a false.

print("keys:",dict3.keys())
print("values:",dict3.values())
print("dict items:",dict3.items())
dict5={'address':'chennai'}
dict3.update(dict5)
print("after update:",dict3)
print("Set default:",dict3.setdefault('age',None))
dict3.popitem()
print( "after pop item:",dict3)
dict3.pop('age')
print("after pop:",dict3)
print("has key:",dict3.has_key('gender'))