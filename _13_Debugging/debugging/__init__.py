import pdb
list = []
for i in range(10, 20):
    if i % 2 == 0 and i % 8 == 0:
        list.append(i)

pdb.set_trace()
print(list)