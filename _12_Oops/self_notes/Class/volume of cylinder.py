class Cylinder:
    pi=3.14
    def __init__(self,radius,height):
        self.radius=radius
        self.height=height

    def volume(self):
        return Cylinder.pi*self.radius**2*self.height
    @classmethod
    def description(cls):
        return "Cylinder class computes the volume using pi={cla.pi}"