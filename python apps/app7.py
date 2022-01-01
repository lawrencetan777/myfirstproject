# Create a list by picking an odd-index items from the first list and even index items from the second
ZombiesA=["bucket-zombie", "regular-zombie", "Dr. Zomboss", "Cone-zombie", "newspaper-zombie", "Gargantuar"]
zombiesB = ["baloon-zombie", "pharoah-zombie", "DJ-zombie", "pirate-zombie", "imp zombie"]
def createteam(a, b):
    team =[]
    aindex = 0
    for k in a:
        if aindex % 2 != 0:
            team.append(k)
        aindex=aindex + 1
    bindex = 0
    for g in b :
        if bindex % 2 == 0:
            team.append(g)
        bindex = bindex + 1


    print(team)


createteam(ZombiesA,zombiesB)