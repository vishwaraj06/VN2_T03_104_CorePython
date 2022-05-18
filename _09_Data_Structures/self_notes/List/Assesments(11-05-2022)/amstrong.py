class Amstrong:
    def __init__(self, number):
        self.num = number
    def isArmstrong(self):
        temp = self.num
        res = 0
        while (temp != 0):
            rem = temp % 10
            res += rem ** 3
            temp //= 10
        if self.num == res:
            print(self.num, "is Armstrong")
        else:
            print(self.num, "is not Armstrong")
if __name__ == "__main__":
    num = 153
    a= Amstrong(num)
    a.isArmstrong()
