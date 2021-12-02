

shirt = {1:"tshirt" , 2:"longSleeves" , 3:"tuxedo",4:"polo-shirt"}
pants = {1:"jeans", 2:"shorts", 3:"dressPants" , 4:"sweatpants"}
shoes = {1:"sneakers", 2:"highHeels", 3:"boots" }
import random
def createrandomOutfit(number):
   z = 0
   while z < number:
     i = random.randint(1,len(shirt))
     newShirt = shirt[i]
     i = random.randint(1,len(pants))
     newPants = pants[i]
     i = random.randint(1,len(shoes))
     newshoes = shoes[i]
     z = z + 1
     print("Your new outfit is "+ newShirt +" , " + newPants + " , and "+newshoes)

   

createrandomOutfit(5)