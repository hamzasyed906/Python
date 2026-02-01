import random

print("Welcome to Rock, Paper, Scissors")

rock = "✊"
paper = "📄"
scissor = "✂️"

options = (scissor, paper, rock)

def playgame():
    compturn = random.choice(options)

    plmove = input("What is your move? Choose rock, paper, or scissor ")

    if plmove == "rock":
        plmove = rock

    elif plmove == "paper":
        plmove = paper

    elif plmove == "scissor":
        plmove = scissor

    else:
        print("Invalid input.")
        return

    print(compturn, "VS", plmove)

    if compturn == plmove:
        print("Draw")

    elif (compturn == rock and plmove == scissor or
          compturn == scissor and plmove == paper or
          compturn == paper and plmove == rock):
        print("Bot Won!")

    elif (plmove == rock and compturn == scissor or
          plmove == scissor and compturn == paper or
          plmove == paper and compturn == rock):
        print("Player Won")

    else:
        print("ERROR")

while True:
    playgame()
    again = input("Play again? (yes/no): ").lower()

    if again != "yes":
        print("Thanks for playing!")
        break
