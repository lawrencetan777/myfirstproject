import random
diceans = []

dice_1 = [1,5,10,3,7,2]
dice_2 = [2,3,3,4,3,8]
dice_3 = [2,2,2,9,9,7]
dice_4 = [1,2,3,4,5,6]
def roll(dice):
    value = random.randint(0,5)
    return dice[value]

diceans[1] = input("Choose 1 dice out of 4 ")
diceans[2] = input("Now choose another" )

