import math


z = [23,12,34,31,31]


def sortalist(list):
 sorted_list = []
 p = 0
 smallestindex = 0
 index  = 0
 
 smallest = 999999999999999999999999999999
 while len(list) != 0:
    index=0
    smallest = 99999999999999999999999
    for a in list:
        if smallest > a:
            smallest = a
            smallestindex = index
        index = index + 1
    r = list.pop(smallestindex)
    sorted_list.insert(p,r)
    p = p + 1


 return sorted_list

 
def central_tendency(data, type):
    sum = 0
    newdata = sortalist(data)
    if (type == "mean"):
        for z in newdata:
            sum = sum+ z
        return sum / len(newdata)
    
    
    if (type == "mode"):
        possmode  = 0
        amountofmode = 0
        
        for f in newdata:
            d = newdata.count(f)
            if d > amountofmode:
                amountofmode = d
                possmode = f
        return possmode

    if (type == "median"):
        median = 0
        if (len(newdata) % 2 != 0):
            median = newdata[math.ceil(len(newdata)/2)]
        else:
            median = central_tendency([newdata[len(newdata)/2+1],newdata[len(newdata)/2 -1]],"mean")
        return median


             



    

print(central_tendency(z, "median"))
       
