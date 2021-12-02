

z = [3,75,8493,-56,56]

def sortalist(list):
 sorted_list = []
 p = 0
 smallestindex = 0
 index  = 0
 
 smallest = 55555556554544
 while len(list) != 0:
    index=0
    smallest = 55555556554544
    for a in list:
        if smallest > a:
            smallest = a
            smallestindex = index
        index = index + 1
    print(str(smallestindex))
    r = list.pop(smallestindex)
    sorted_list.insert(p,r)
    p = p + 1


 print(sorted_list)

 
    

sortalist(z)