# Problem 2 : Convert roman numeral to integer XVI


def conversionmachine(expression, operator, expression2):
    lookup = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    lastNum = 1
    arabicnum = 0
    arabicnum2 = 0
    lastnum2 = 1
    i = len(expression) - 1
    while i >= 0:
        num = lookup[expression[i]]
        if num < lastNum:
            arabicnum = arabicnum - num
        else:
            arabicnum = arabicnum + num

        lastNum = num

        i = i - 1
    z = len(expression2) - 1
    while z >= 0:
        num2 = lookup[expression2[z]]
        if num2 < lastnum2:
            arabicnum2 = arabicnum2 - num2
        else:
            arabicnum2 = arabicnum2 + num2

        lastnum2 = num2

        z = z - 1
    result = 0
    if operator == "+":
        result = arabicnum + arabicnum2
    elif operator == "-":
        result = arabicnum - arabicnum2
    elif operator == "*":
        result = arabicnum * arabicnum2
    elif operator == "/":
        result = arabicnum / arabicnum2
    else:
        result = "operator error"
    return result


print(conversionmachine("MCMLVI", "+", "XIX"))
