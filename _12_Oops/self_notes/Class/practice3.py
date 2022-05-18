class Crypto:
    a="coinmarket"
    b="INR"
    def __init__(self,coin_name,coin_value,coin_start,coin_end,coin_holder):
        self.coin_name=coin_name
        self.coin_value=coin_value
        self.coin_start=coin_start
        self.coin_end=coin_end
        self.coin_holder=coin_holder

    def new(self):#method with instance variable followers,
        # instance attributes are those attributes that are not shared by objects.
        # Every object has its own copy of the instance attribute.
        print("Coin Details:",self.coin_name,self.coin_value,self.coin_start,self.coin_end,self.coin_holder,Crypto.a,Crypto.b)
#        print("Coin Details:",self.coin_name,self.coin_value,self.coin_start,self.coin_end,self.a,self.b)


x=Crypto("BTC",34000,32000,34000,2000)
x.new()
y=Crypto("YRN",122,333,445,667)
y.new()
