
# Exception handling
'''
Traceback (most recent call last):
  File "C:/Users/madhu/git_projects/Batch_16/B16_PythonTraining/_14_Exception_handling/mypractice/test1.py", line 11, in <module>
    print("Result is ", in_val + 10)
TypeError: must be str, not int
'''
print("--Before list----")
list1 = [11, 22, 33, 45]
print(list1[4])
print("--After list----")
in_val = input("Enter value : ")  # '5'
print("Result is ", in_val + 10)
print("End of program")
