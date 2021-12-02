
# find biggest family in phone book
phone_book = [
    ["John Doe", "123456"],
    ["Bob Cat", "374637"],
    ["Log Chop", "123456"],
    ["Hot Dog", "726373"],
    ["Log Chop Jr", "123456"],
    ["Log Chop III", "123456"],
    ["Log Chop IV", "123456"],
    ["Puma Cat", "374637"],
    ["Lion Cat", "374637"],
    ["Tiger Cat", "374637"],
    ["Leopard Cat", "374637"],
    ["Jaguar Cat", "374637"]
]

def find_biggest_family(phones):
    phoneDict = {}
    greatestfamnum = 2000
    greatestfamamount = -1
    
    for s in phones:
        if s[1] not in phoneDict:
            phoneDict[s[1]] = []
        phoneDict[s[1]].append(s[0])
    for z in phoneDict:
        if len(phoneDict[z]) > int(greatestfamamount):
            greatestfamamount = len(phoneDict[z])
            greatestfamnum = z
        
    familybig = phoneDict[greatestfamnum]
    print(familybig)

find_biggest_family(phone_book)
    
    


    

    

# family is a list or set containing "John Doe" and "Log Chop"


