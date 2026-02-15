class element():
    def __init__(self, mass, percent):
        self.mass = mass
        self.percent = percent

list = [element(12, .989), element(13.21, .0106), element(14 ,.0004)]

def weightedAvg(list):
    percent = 0
    avg = 0
    for i in list:
        percent = percent + i.percent
        if percent > 1:
            return Exception
        avg = avg + (i.percent * i.mass)

    return avg


print(weightedAvg(list))
