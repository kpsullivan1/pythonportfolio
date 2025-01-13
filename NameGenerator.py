#Kelsey Sullivan
print("Welcome to what Gossip Girl Character are you!")
print("Please answer all questions to see your results")
ans= input("Silver(S) or Gold(G)")
if ans=="S":
    ans= input("Nice(N) or Intelligent(I)")
    if ans=="I":
        ans= input("Headband(HBD) or Sunglasses(SUN)")
        if ans== "HBD":
            print("You are Blair Waldorf")
        else:
            print("You are Georgina Sparks")
    if ans=="N":
        ans= input("Blogging(BG)) or Politics(P)")
        if ans== "BG":
            print("You are Serena Van der Woodsen")
        else:
            print("You are Nate Archibald")
if ans=="G":
    ans= input("Successful(SUC) or Unique(U)")
    if ans=="SUC":
        ans= input("Business(BSS) or Fashion(FAS)")
        if ans== "BSS":
            print("You are Chuck Bass")
        else:
            print("You are Jenny Humphrey")
    if ans=="U":
        ans= input("Movies(M)) or Books(B)")
        if ans== "M":
            print("You are Vanessa Abrams")
        else:
            print("You are Dan Humphrey")
