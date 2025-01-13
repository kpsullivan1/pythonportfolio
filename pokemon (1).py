#Kelsey Sullivan
#pokeman evolution game
#initialize
import random
pokemon_level=0
pokemon_name="horsea"
day=1
#functions
def horsea():
    print("""⠀⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟦🟦⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜🟦🟦🟦🟦⬛⬛⬜⬜⬜🟦⬛⬜🟦⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜🟦🟦🟦🟦🟦🟦⬛⬛⬛⬜🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬜⬜⬜⬜🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜🟦🟦⬜⬜🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟦⬛🟦🟦🟦🟦🟦⬛⬜⬜⬛🟦🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬜⬜⬛🟦🟦🟦🟦⬛⬛⬜⬜⬛🟦🟦🟦⬛⬛⬛⬛🟦⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬜⬛⬛🟦🟦🟦🟦⬛⬜⬛⬜⬛🟦🟦🟦🟦🟦🟦⬜⬜⬛⬜⬜⬛⬛⬜⬜
⬜⬜⬜⬜⬛⬜⬛🟦🟦🟦🟦⬛⬛⬛⬜⬛🟦🟦🟦🟦🟦🟦⬛⬛⬜⬛⬛🏻🏻⬛⬜
⬜⬜⬜⬜⬛🟦⬛⬜🟦🟦🟦⬛🟦⬛⬜⬛🟦🟦🟦🟦⬛⬛⬜⬜⬛🏻🏻🏻🏻🏻⬛
⬜⬜🟦🟦⬛⬛⬜🟦🟦🟦🟦🟦⬛⬛⬜🟦🟦🟦🟦⬛⬛⬜⬜⬛🏻🏻🏻🟦🟦🟦⬛
⬜🟦⬜⬜⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛🏻🏻🟦🟦🏻🏻🏻⬛
🟦⬜⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛🟦🟦🟦🟦⬛🟦🏻🏻🏻🏻🏻⬛
🟦⬜⬛⬛🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦🟦🟦⬛🟦⬛⬛⬛⬛🏻🏻🏻🏻🟦🟦⬛⬜
⬛⬜⬛⬛⬛🟦🟦🟦⬛🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦⬛🟦🏻🏻🟦🟦🟦🏻🏻⬛⬜
⬜⬛🟦⬛⬛🟦🟦⬛⬜⬛⬛⬛⬛⬛🟦🏻🏻🟦🟦🟦🟦⬛⬛⬛🏻🏻🏻⬛⬛⬜⬜
⬜⬜⬛🟦🟦⬛⬛⬜⬜⬜⬜⬜⬛⬜🏻🏻🏻🏻⬛🟦🟦🟦🟦⬛⬛⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜🟦⬜⬜🏻⬛⬛🏻🟦🟦🟦🟦🟦🟦⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🏻🏻🏻🏻🟦🟦🟦🟦🟦🟦⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟦⬜🏻🏻⬛⬛⬛🟦🟦🟦🟦🟦🟦🟦⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🏻⬛🟦🟦🟦⬛🟦🟦🟦🟦🟦🟦⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜🟦🟦⬛🟦🟦🟦🟦🟦🟦⬛⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟦⬜⬜⬜🟦🟦🟦⬛🟦🟦🟦🟦🟦⬛⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟦⬜⬜⬜⬛🟦🟦🟦⬛🟦🟦🟦🟦🟦⬛⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜🟦⬛🟦🟦🟦⬛🟦🟦🟦🟦🟦⬛⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦🟦⬛⬛⬛🟦🟦🟦🟦🟦🟦⬛⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟦🟦🟦🟦🟦⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜""")
def seadra():
    print("""⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬜⬛🌫️🌫️⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬜⬛🌫️🌫️⬛🌫️🌫️⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛🌫️⬛🌫️🌫️⬛🌫️🌫️⬛🌫️🌫️⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛🌫️⬛🌫️⬛🌫️🌫️⬛🌫️🌫️⬛⬛⬜⬜⬛⬛⬛⬜⬜⬜⬜
⬜⬛🌫️⬛🌫️🌫️🌫️🌫️🌫️🌫️🌫️⬛🟦🟦⬛⬛🌫️🌫️⬛⬜⬜⬜⬜
⬜⬛🌫️⬛🌫️🌫️🌫️🌫️🌫️🌫️🌫️🟦🟦⬛🌫️🌫️🟦⬛⬜⬜⬜⬜⬜
⬜⬜⬛🌫️⬛🌫️⬛🌫️🌫️⬛⬛🟦🟦🟦🟦⬛⬛🌫️⬛⬜⬛⬛⬛
⬜⬛⬛⬛🌫️🌫️⬛⬜⬛⬜🟦🟦🟦🟦🟦🌫️🟦🟦⬛⬛🏻🏻⬛
⬛🌫️🌫️🟦🟦🟦🟦⬛⬛🟦🟦🟦⬛🟦🟦🟦⬛⬛🌫️🏻🏻⬛⬜
⬛🌫️⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛🟦🟦⬛🌫️🏻⬛⬜⬜
⬜⬛🟦🟦⬛⬛⬛🟦🟦🟦🟦⬛🟦🟦⬛⬛⬛🌫️🌫️⬛⬛⬛⬜
⬜⬜⬛⬛⬜⬜⬛⬛⬛⬛⬛🟦🟦🟦🟦🟦🟦🟦🌫️🏻🏻🏻⬛
⬜⬜⬜⬜⬜⬜⬛🏻🏻🏻🏻🟦🟦⬛⬛🟦🟦🟦⬛⬛⬛⬛⬜
⬜⬜⬜⬜⬜⬜⬜⬛🏻⬛⬛🏻🟦🟦🟦⬛⬛🏻🏻⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛🌫️🌫️⬛🏻🟦🟦⬛⬜⬛⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛🌫️🌫️⬛🟦⬛🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛🟦🌫️⬛⬛🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜""")
def kingdra():
  print("""                       X   XX
                       X XXXX
                      X XX X
                      XXX  X
                XXXXXX     XX
          XXX XXX             XX
      XXXX           XXX       XX
    XXXXX           XXXX       XX
  XXX   X                       X
 X  X    X                      X
         XX XX         XX       X
XXXXXXXXXXX  XXX  XXXXXX        X           XXXXX
                  XX   X        XXX             XX
                  XX XXX         XX       XXX XX
                  X    X          XX      XXX  X
                  XXXX X           X     XXXXX X  X
                  X     X          XXXX XX XX    XX
                  X     X           XXXX   XXX XXX
                  XXXXXXX                 XX
                   X    XX              XX
                    XX   XX           XXX
                      XXXXXX         XX
                            XXXXXXXXX              """)
def name():
  global pokemon_name
  if pokemon_level<=5:
    pokemon_name="horsea"
    print(pokemon_name)
    horsea()
  elif pokemon_level >5 and pokemon_level<=10:
    pokeman_name="seadra"
    print(pokemon_name)
    seadra()
  else:
    pokeman_name="kingdra"
    print(pokemon_name)
    kingdra()
def menu():
  global pokemon_level
  global day
  global pokemon_name
  while True:
        print("Welcome to the pokemon evolution game! You are on day:"+ str(day))
        print("Please select an action from the menu: ")
        print("""1. Train
2. Gym Battle
3. Rest
4. Exit""")
        action=int(input("(1-4) Option:"))
        if action==1:
          pokemon_level=pokemon_level+1
          day=day+1
          print("Your training increased your level by 1. Your new score is:")
          print(pokemon_level)
          print("Your Pokemon is:")
          name()
        if action==2:
          value=random.randint(1,2)
          if value==1:
            print("You won your battle! Your score will increase by 2. Your new score is:")
            pokemon_level=pokemon_level+2
            day=day+1
            print(pokemon_level)
            print("Your Pokemon is:")
            name()
          if value==2:
            print("You lost your battle, so your score will not increase.")
            day=day+1
        if action==3:
          print("Your pokemon is resting. Your score is still:")
          print(pokemon_level)
          print("Your Pokemon is:")
          name()
          day=day+1
        if action==4:
          print("Thank you for using Pokemon Evolution! Your final pokemon is:")
          name()
          break

#main
menu()

