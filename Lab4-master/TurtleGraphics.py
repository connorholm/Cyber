#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(myTurtle, sides):
    for i in range(sides):
        myTurtle.forward(50)
        myTurtle.right(360/sides)
    

def testing(myTurtle, number):
    myTurtle.color("blue")
    myTurtle.title("Joss Bot")
    myTurtle.penup()
    myTurtle.forward(100)
    myTurtle.pendown()
    myTurtle.forward(100)

def fillCorner(myTurtle, number):
    myTurtle.color("red","blue")
    myTurtle.begin_fill()
    if number >= 3:
        myTurtle.right(180)
    for i in range(4):
        myTurtle.forward(500)
        if (number % 2) == 1:
            myTurtle.left(90)
        else:
            myTurtle.right(90)
    myTurtle.end_fill()

def squaresInSquares(myTurtle, sqNum):
    myTurtle.color("green","yellow")
    myTurtle.up()
    myTurtle.back(200)
    myTurtle.left(90)
    myTurtle.forward(200)
    myTurtle.right(90)
    myTurtle.down()
    index = 0
    for i in range(sqNum):
        if (index+1) == sqNum:
            myTurtle.begin_fill()
        size = 400-(2*index*20)
        drawSquare(myTurtle, size)
        if (index+1) == sqNum:
            myTurtle.end_fill()
            break
        myTurtle.forward(20)
        myTurtle.right(90)
        myTurtle.up()
        myTurtle.forward(20)
        myTurtle.down()
        myTurtle.left(90)
        index = index+1

def main():
    myTurtle = turtle.Turtle()
    # drawSquare(myTurtle, 50)
    #drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon

    #fillCorner(myTurtle, 1) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    squaresInSquares(myTurtle, 3) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
input("Hit enter to quit") #this keeps the turtle window from disapearing too soon.
