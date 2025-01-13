#kelsey
#init
import random
def multiplication():
    score=0 #int
    qnum=0 #int
    print("hello, and welcome to the multiplication game")
    difficulty=input(("please select your difficulty, easy, medium, hard")) #str that takes difficulty
    questions=int(input(("please input the number of questions you would like"))) #int that takes q number
    if difficulty=="easy":
        for i in range(questions):
            num1=random.randint(0,4) #int generates random number
            num2=random.randint(0,4) #int generates random number
            product=int(num1*num2) #int that is the correct answer
            ans=int(input(("what is "+ str(num1)+" times "+str(num2)))) #int that takes their answer
            if ans==product:
                print("correct!")
                score=score+1
                qnum=qnum+1
            else:
                print("incorrect")
                qnum=qnum+1

    if difficulty=="medium":
        for i in range(questions):
            num1=random.randint(4,8) #int generates random number
            num2=random.randint(4,8) #int generates random number
            product=int(num1*num2) #int that is the correct answer
            ans=int(input(("what is "+ str(num1)+" times "+str(num2)))) #int that takes their answer
            if ans==product:
                print("correct!")
                score=score+1
                qnum=qnum+1
            else:
                print("incorrect")
                qnum=qnum+1
    if difficulty=="hard":
        for i in range(questions):
            num1=random.randint(8,12) #int generates random number
            num2=random.randint(8,12) #int generates random number
            product=int(num1*num2) #int that is the correct answer
            ans=int(input(("what is "+ str(num1)+" times "+str(num2)))) #int that takes their answer
            if ans==product:
                print("correct!")
                score=score+1
                qnum=qnum+1
            else:
                print("incorrect")
                qnum=qnum+1
    print("your score is "+ str(score)+ " out of " + str(qnum))
multiplication()

