#Count characters in string
# 1.inbuild method:
x="Google LLC is an American multinational technology"
text=x.count("a")
print("Count is:",text)

# 2.loops:
x="Google LLC is an American multinational technology"
count=0
for i in x:
    if i=="a":
     count+=1
print("count of a is:",count)

#3 functions
def count(x):
    x = "Google LLC is an American multinational technology"
    count=0
    for i in x:
        if x=="a":
          count+=1
print(count(x))


#4. if else
x ="Google LLC is an American multinational technology"
count=0
if x=="a":
    count=count+1
    print("Characters count of a is:",x.count())
else:
    print("None")





