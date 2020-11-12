#ApproxPi.py
#Name:
#Date:
#Assignment:
import math
import time

def main():
    realPi = math.pi

    #ask user for decimal percision (up to 10)

    start = time.time()
    #calculate pi using the approximation technique
    #Loop until the level of percision is reached

    end = time.time()

    elapsedTime = end - start
    print(elapsedTime)

main()
