class Students:
    school="Lions matriculation Hr Sec School"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(self.name,self.age,"school",Students.school)

    @classmethod
    def change(cls,school):
        cls.school=school

    def show(self):
        print(self.name+"'s age is:"+str(self.age))

raja=Students("raja",29)
raja.show()
tharun=Students("Tharun",24)
tharun.show()