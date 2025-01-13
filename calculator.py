#kelsey sullivan

#init

#funct
def add(int1,int2):
    print( int1+int2)
def subtract(int1,int2):
    print(int1-int2)
def multiply(int1,int2):
    print(int1*int2)
def divide(int1,int2):
    print(int1/int2)
def calc():
    while True:
        print("welcome to the simple calculator")
        print("please select an opperation: ")
        print("""1. add
2. subtract
3. multiply
4. divide
5. quit""")
        operation=int(input("(1-5) Option:"))
        if operation==1:
            num1= int(input("enter the first number"))
            num2= int(input("ener the seccond number"))
            add(num1,num2)
        if operation==2:
            num1= int(input("enter the first number"))
            num2= int(input("ener the seccond number"))
            subtract(num1,num2)
        if operation==3:
            num1= int(input("enter the first number"))
            num2= int(input("ener the seccond number"))
            multiply(num1,num2)
        if operation==4:
            num1= int(input("enter the first number"))
            num2= int(input("ener the seccond number"))
            divide(num1,num2)
        if operation==5:
            print("use this calculator again soon")
            break
#main
calc()

