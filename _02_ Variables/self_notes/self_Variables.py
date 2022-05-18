a=12
b=13.5
c='Raja'
print(a,b,c)
print(type(a),type(b),type(c)) # data types of variables
print(id(a),id(b),id(c)) # print memory locations
print('***************************************************')

#casting (conversting of data into int,str,float)
print(float(a)) # convert int into float
print(int(b))  #convert float into int
print(complex(a)) #convert int into Complex
print('***************************************************')

# Multiple variables
x=y=z= 12
print(x,type(x),id(x))
print(y)
print(z)
print('***************************************************')


# String
new='i love my country'
print(new[3]) # indexing start from 0,1,2,3,4,5,6,7,n
print(new[2:7])# indexing by ranging
print(new[-4]) # Negative indexing
print(new[-6:-2]) # Negative indexing range
print(len(new)) # prints the lenth of the given string
print(new.upper()) # convert the given string into upper case
print(new.replace('my','our')) # replace the string with new one
print(new *2) # prints string two times
print('***************************************************')


 ####Check string######
 #1.(in) to check the phrase or word present in the string[True or False]
check_string="Hello world"
print ("Hello" in check_string)
print ("Hello" not in check_string)
print('***************************************************')

#### concatination of string####

new1="Raja"
new2="Tharun"
print(new1+new2)

####concatination of string and number###
new3=54566644
new4="Tharani{}"
print(new4.format(new3))

####multiple arguments###
new5=1998
new6=1990
new7="Raja{} Tharani{}"
print(new7.format(new6,new5))

# LIST
list=[12,'raja',13.5,12,'tharun','Raj']
print(list)
print(list[2]) # access the list using indexing
print(list[-5]) #accessing the list using negative indexing
print(list[0:3]) # Accessing the list using range of indexing
list[2]='varun'# modify the list
print(list)
list.append("Nitwik")#add items into list
print(list)
list.insert(2,"XXX")# insert items into list usin indexing
print(list)
print('***************************************************')