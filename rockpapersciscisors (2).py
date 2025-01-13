#kelseySullivan
#init
import random
wins=0
losses=0
ties=0
#functions
def win():
    global wins
    print("you win")
    wins=wins+1
def lose():
    global losses
    print("you lose")
    losses=losses+1
def tie():
    global ties
    print("you tied")
    ties=ties+1
def rockPaperScisors():
    while True:
        print("welcome to rock paper scisors")
        loop=input("would you like to play? y or n")
        if loop=="y":
            ans=input("what is your move?(rock, paper, scisors)")
            ans=ans.lower()
            comp=random.randint(1,3)
            if ans=="rock":
                if comp==1:
                    print("the computers move was scisors")
                    win()
                if comp==2:
                    print("the computers move was paper")
                    lose()
                if comp==3:
                    print("the computers move was rock")
                    tie()
            if ans=="paper":
                if comp==3:
                    print("the computers move was rock")
                    win()
                if comp==1:
                    print("the computers move was scisors")
                    lose()
                if comp==2:
                    print("the computers move was paper")
                    tie()
            if ans=="scisors":
                if comp==2:
                    print("the computers move was paper")
                    win()
                if comp==3:
                    print("the computers move was rock")
                    lose()
                if comp==1:
                    print("the computers move was scisors")
                    tie()
        if loop=="n":
            print("wins=" + str(wins)+ " losses=" + str(losses)+ " ties=" +str(ties))
            break

rockPaperScisors()
