#RPS.py
#Name: Connor Holm
#Date:
#Assignment:
import random

def main():
    wins = 0
    ties = 0
    losses = 0
    #Create a loop that continues as long as the user wants to play.
    #User can play as many games as they wish.
    playAgain = True
    while playAgain:
        user = input("Select Rock, Paper, or Scissors (R, P, S): ")
        #Randomly choose the computer between 'R', 'P', or 'S'
        cpu = random.choice(["R","P","S"])
        #Prompt the user for their RPS selection
        print("User: "+user)
        print("Computer: "+cpu)
        #Determine winner and state what happened to the user
        if (cpu == user):
            ties = 1 + ties
        elif (cpu == "R" and user == "P") or (cpu == "P" and user == "S") or (cpu == "S" and user == "R"):
            wins = 1 + wins
        else:
            losses = 1 + losses
        #Ask the user if they would like to play again.
        if input("Would you like to play again (Yes/No): ") == "Yes":
            playAgain = True
        else:
            playAgain = False
    #In the end, print the stats
    print("Wins \t Ties \t Losses")
    print("---- \t ---- \t ------")
    print(wins, "\t", ties , "\t", losses)

main()
