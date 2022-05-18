class Match:
    def __init__(self, odi, score, avg, strike):
        self.odi = odi
        self.score = score
        self.avg = avg
        self.strike = strike

    def new(self):
        print("Batsman:", self.odi, self.score, self.avg, self.strike)


sachin = Match(250, 115, 45, 60)
sachin.new()
shewag = Match(120, 7800, 41, 51)
shewag.new()
