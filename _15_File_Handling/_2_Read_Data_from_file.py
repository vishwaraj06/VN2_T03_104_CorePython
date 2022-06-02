print("--------------File read Operations--------------")
'''
1. Open file
2. Perform operations read/write
3. Close the file 

'''

# my_sring = 'harsha in the class'
# split1 = my_sring.split(' ')
# print(type(split1))
my_file = open("read_data1.txt", 'r')   # 1
f_data = my_file.read()   # 2
'''
print("content type :", type(f_data))
print("File content :", f_data)
print("After splitting :", f_data.split("\n"))
print("--------------")
'''
my_file.close()  # 3


# Businees Logic

# Check word count of  'Python'  in write_data.txt
counter = 0
# ascii values python > Python
for line in f_data.split("\n"):
    print(line)
    if "Python" in line:
        counter += 1
        print("**** :", line)

print("Python word repeated times in file : ", counter)

my_file.close()  # 3


print("----------Using functions---------")

def find_word_count(file, word):
    f_obj = open(file, 'r')
    f_data = f_obj.read()
    counter = 0
    for line in f_data.split("\n"):
        if word in line:
            counter += 1
            #print("**** :", line)

    print("Python word repeated times in file : ", counter)

f_name = "read_data1.txt"
s_word = input("Enter word to search : ")
find_word_count(f_name, s_word)

print("----------Using Exception handling---------")
print("----------Using OOPS instance method---------")
print("----------Using OOPS class method---------")
print("----------Using OOPS static method---------")