#DiceRoll.py
#Name: Connor Holm
#Date:
#Assignment:
import random

def main():
    #Create an empty list with possible roll values
    diceArray = [0,0,0,0,0,0,0,0,0,0,0,0]
    #Create two dice values ranging from 1 - 6 each
    for i in range(1000):
        dice1 = random.choice(range(1,7))
        dice2 = random.choice(range(1,7))
        #find the sum total of the two dice
        total = dice1 + dice2
        diceArray[total-1] = diceArray[total-1] + 1
    
    #print statictics for dice rolls
    index = 0
    print("Frequency of Dice Rolls: ")
    for number in diceArray:
        indexTotal = index+1
        print(str(indexTotal)+": "+str(number))
        index = index + 1
main()
