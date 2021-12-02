
# Problem 2 : Convert roman numeral to integer XVI

def conversionmachine(expression):
    lookup = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    lastNum = 1
    arabicnum = 0
    i  = len(expression) - 1
    while i >=0:
        num = lookup[expression[i]]
        if num < lastNum:
            arabicnum = arabicnum - num
        else:
            arabicnum = arabicnum + num
        
        lastNum = num

        i= i-1
    return arabicnum

print(conversionmachine("LVI"))


