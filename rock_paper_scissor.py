import random

Cchoice = ["Rock", "Paper", "Scissor"]  # for computer to choose
while True:
    youwin, compwin = 0, 0
    print("Welcome to Rock paper scissor game")
    for i in range(1, 6):    # 1 to 5 rounds
        print("Round ", i, "starts...")
        print("Select your choice:")
        print("Enter", "1 for Rock", "2 for paper", "3 for scissor", sep="\n")
        you_choose = int(input())
        if you_choose == 1:
            your_choice = "Rock"
        elif you_choose == 2:
            your_choice = "Paper"
        elif you_choose == 3:
            your_choice = "Scissor"
        else:
            your_choice = "None"
        print("You select: ", your_choice)
        if your_choice == "None":
            print("Invalid input...Game Ends")
            break
        comp_choice = random.choice(Cchoice)
        print("Computer select: ", comp_choice)
        if your_choice == comp_choice:
            print("Round draw")
        elif (your_choice == "Rock" and comp_choice == "Scissor") or (your_choice == "Paper" and comp_choice == "Rock") or (your_choice == "Scissor" and comp_choice == "Paper"):
            youwin += 1
            print("You win this round")
        else:
            compwin += 1
            print("Computer win this round")
        print("-------------------------------------------")
        # for loop ends
    print("Your score after 5 rounds: ", youwin)
    print("Computer's score after 5 rounds: ", compwin)
    if youwin > compwin:
        print("Congrats!! You win the game")
    elif youwin < compwin:
        print("Computer won the Game....Better Luck next time!!")
    else:
        print("Match draw")

    user_choice = input("To continue the game enter (Yes)..anything else to exit")
    print("******************************************")
    if user_choice == "Yes" or user_choice == "yes" or user_choice == "YES":
        continue
    else:
        break
    # end of while end of program
