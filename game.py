import random

Things = ['rock', 'paper', 'scissor']

Tries = 0
user_Score = 0
coumputer_Score = 0

while Tries <= 3:
    user_input = input("Enter your choice!: ")
    computer_input = random.choice(Things)
    if user_input in Things:
        if user_input == "rock" and computer_input == "scissor":
            print("Computer choose " + computer_input)
            print("You got a point")
            print("\n")
            user_Score += 1
            Tries += 1
        elif user_input == "rock" and computer_input == "paper":
            print("Computer choose " + computer_input)
            print("Computer got a point!")
            print("\n")
            coumputer_Score += 1
            Tries += 1
        elif user_input == "paper" and computer_input == "rock":
            print("Computer choose " + computer_input)
            print("You got a point")
            print("\n")
            user_Score += 1
            Tries += 1
        elif user_input == "paper" and computer_input == "scissor":
            print("Computer choose " + computer_input)
            print("Computer got a point!")
            print("\n")
            coumputer_Score += 1
            Tries += 1	
        elif  user_input == "scissor" and computer_input == "paper":
            print("Computer choose " + computer_input)
            print("You got a point")
            print("\n")
            user_Score += 1
            Tries += 1
        elif  user_input == "scissor" and computer_input == "rock":
            print("Computer choose " + computer_input)
            print("Computer got a point!")
            print("\n")
            coumputer_Score += 1
            Tries += 1
        else:
            print("Computer choose " + computer_input)
            print("No one scored the point")
            print("\n")
            Tries += 1
    else:
        print("wrong input")
    

if user_Score > coumputer_Score:
    print("You won!")
    print("\n")
elif coumputer_Score > user_Score:
    print("You lost")
    print("\n")
else:
    print("It's a draw game!")
    print("\n")

print("Your Score is ", user_Score, ".")
print("Computer score is " + str(coumputer_Score) + ".")
