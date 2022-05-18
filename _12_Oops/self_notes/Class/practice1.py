class Students:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def get_data(self):
        print("Studenst datails:", self.name, self.age, self.city)


raju = Students("Raja", 23, "salem")
raju.get_data()
gowri = Students("gowri", 24, "salem")
gowri.get_data()
