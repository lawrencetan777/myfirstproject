y = []
import random


def filterfromRange(min, max, num):
    for s in range(min, max):
        if s % num == 0:
            print(s)


def filterfromStringOrlist(stringorList, step):
    i = 0
    x = [stringorList[0]]
    for s in stringorList:
        if i == step:
            x.append(s)
            i = 0
        i = i + 1
    print(x)


def arandomfunct(string):
    r = []
    for e in string:
        r.append(e)
    random.shuffle(r)

    filterfromStringOrlist(r, 2)


i = 0
while i < 6:
    arandomfunct("CakeCakeCake")
    i = i + 1
pants = dict([("jeans", 1), ("dress-pants", 2), ("sweatpants", 3)])
print(pants["jeans"])
cakeflavor = input("What is your favorite cake flavor? ")
print(cakeflavor)
