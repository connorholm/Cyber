#MadLib.py
#Name: Connor Holm
#Date: 11/10/2020
#Assignment:


def main():
    #Ask user for words
    N = input("Type 3 noun with spaces between: ")
    V = input("Type 3 verbs with spaces between: ")
    print(N+V)
    nouns = N.split()
    verbs = V.split()
    #Print the story with the user supplied words.
    print(
        "The "+verbs[0]+" "+nouns[0]+" liked "+verbs[1]+" into the "+nouns[1]+". The "+nouns[2]+" "+verbs[2]+" onto the roof."
    )

main()
