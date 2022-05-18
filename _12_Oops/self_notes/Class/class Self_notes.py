class Car:
    x=20
    y=10
    def sum_x_y(self):# class methods  ,Self (object self reference)
        print("add:",self.x+self.y)
    def new(self,my_arg,num):
        print(my_arg,num)
mycar=Car()
print(mycar.x,mycar.y)
mycar.sum_x_y()#call methods
mycar.new("hello",'20')
