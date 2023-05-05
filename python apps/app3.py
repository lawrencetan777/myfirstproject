

shirt = {1:"t-shirt" , 2:"long sleeves" , 3:"a tuxedo",4:"a polo-shirt", 5:"swimshirt"}
pants = {1:"jeans", 2:"shorts", 3:"dress pants" , 4:"sweatpants", 5:"pajama pants"}
shoes = {1:"sneakers", 2:"high heels", 3:"boots" ,4:"dress shoes", 5:"no shoes" }
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
     print("Your new outfit will be "+ newShirt +", " + newPants + ", and "+newshoes)

   

createrandomOutfit(50)