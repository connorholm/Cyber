#WordCount.py
#Name:
#Date:
#Assignment:

def main():
    textFile = open("/Users/90305163/Developer/Cyber/Lab6-master/gettysberg.txt", 'r')
    words = []
    numWords = 0
    for line in textFile:
        words.append(line.split())
    for line in words:
        for word in line:
            numWords = numWords + 1
    print(numWords)


main()
