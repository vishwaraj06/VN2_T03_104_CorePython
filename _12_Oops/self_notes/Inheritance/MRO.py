class A:
    def process(self):
        print(" In class A")
class B(A):
    def process(self):
        print(" In class B")
class C(B, A):
    def process(self):
        print(" In class C")
# Creating object of C class
C1 = C()
C1.process()
print(C.mro())

#we create three classes named A, B and C. Class B is inherited from A, class C inherits from B and A.
# When we create an object of the C class and calling the process() method,
# Python looks for the process() method in the current class in the C class itself.
#Then search for parent classes, namely B and A, because C class inherit from B and A.
# that is, C(B, A) and always search in left to right manner.