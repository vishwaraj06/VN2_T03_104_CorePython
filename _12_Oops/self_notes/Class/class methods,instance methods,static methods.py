class Crypto:
    a="coinmarket"
    b="INR"
    def __init__(self,coin_name,coin_value,coin_start,coin_end,coin_holder):
        self.coin_name=coin_name
        self.coin_value=coin_value
        self.coin_start=coin_start
        self.coin_end=coin_end
        self.coin_holder=coin_holder

    def new(self):
        print("Coin Details:",self.coin_name,self.coin_value,self.coin_start,self.coin_end,self.coin_holder)

    @classmethod
    def new1(cls):
        print("Count:",cls.a,cls.b)

x=Crypto("BTC",34000,32000,34000,2000)
x.new()
y=Crypto("YRN",122,333,445,667)
y.new()
Crypto.new1()