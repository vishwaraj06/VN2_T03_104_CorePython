n=int(input("Enter value below 10:"))
for i in range (n,0,-1):
    k=i
    for j in range(0,i):
        print(k,end=' ')
    print("")