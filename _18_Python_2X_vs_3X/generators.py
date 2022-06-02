#generator generates iterations,,it creates special iterators inside functions..for this we are going to use keyword "YIELD"


# def demo():
#     return 5
# a=demo()
# print(a)

# def demo():
#     yield 5# it creates generator object id,
# a=demo()
# print(a.__next__())
#
def demo():
    n=1
    while n<=7:
        val=n*n
        yield val
        n=n+1
a=demo()
for i in a:
    print(i)


    #used for specific values retrival,insted of processing all files 