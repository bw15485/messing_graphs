

class averages:
    def __init__(self,bids,asks,bquant,aquant):
        self.bids = bids
        self.asks = asks
        self.bquant = bquant
        self.aquant = aquant

    def midprice(self):
        return (self.bids[0] + self.asks[0])/2

    def microprice(self):
        microprice = (self.bids[0]*self.aquant[0] + self.asks[0]*self.bquant[0])/(self.aquant[0] + self.bquant[0])
        return microprice



week1 = averages([10,8,6,4],[12,15,18,20],[10,1,10,1],[10,1,10,1])

print(week1.midprice())
print(week1.microprice())

print('not cool')