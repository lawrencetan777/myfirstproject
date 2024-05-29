import math

e = [1, 12, 23, 23, 23, 31, 31, 34]
z = [1, 23, 12, 34, 31, 31, 23, 23]


def sortalist(list):
    sorted_list = []
    p = 0
    smallestindex = 0
    index = 0

    smallest = 999999999999999999999999999999
    while len(list) != 0:
        index = 0
        smallest = 99999999999999999999999
        for a in list:
            if smallest > a:
                smallest = a
                smallestindex = index
            index = index + 1
        r = list.pop(smallestindex)
        sorted_list.insert(p, r)
        p = p + 1

    return sorted_list


def central_tendency(data, type):
    sum = 0
    newdata = sortalist(data)

    if type == "mean":
        for z in newdata:
            sum = sum + z
        return int(sum / len(newdata))

    if type == "mode":
        possmode = 0
        amountofmode = 0

        for f in newdata:
            d = newdata.count(f)
            if d > amountofmode:
                amountofmode = d
                possmode = f
        return possmode

    if type == "median":
        median = 0
        if len(newdata) % 2 != 0:
            median = newdata[math.ceil(len(newdata) / 2)]
        elif len(newdata) % 2 == 0:
            median = central_tendency(
                [
                    newdata[int((len(newdata) / 2)) - 1],
                    newdata[int((len(newdata) / 2))],
                ],
                "mean",
            )

        return median
    else:
        return "error"


print(central_tendency(e, "mode"))

print(e)
