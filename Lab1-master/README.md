# Lab 1 - CYBR 2980

## Overview
- Setup GitHub account
  - [GitHub.com](https://www.github.com)
- Create an account on [Repl.it](https://repl.it/)
---
### Atom Editor
- How to configure Python on your home computers
  - Download Python
    - [python.org](https://www.python.org/)
  - Download Atom
    - [Atom.io](https://atom.io/)
  - Install Python-run
    - File -> Settings
    - Install -> python
    - Click Install on the python-run extension
    - Hit F5 on your computer to run your current python script.
### IDLE Editor
- IDE that comes with Python when you download
- Opens to an interactive shell
- You can run scripts by from the **Run** menu and choosing **Run Script**
  - Alternatively you can type **F5** on your keyboard

## Instructions
- Copy the GitHub link for this lab https://github.com/UNO-Babb/Lab1
- In [Repl.it](https://repl.it), click the **New Repl (+)** in the top right corner
- Select **Import from GitHub** and paste the link
- The **.replit** file decides what happens when you click the run button

Now that we have the files on your repl.it, we will start to work with the Python file.

## FirstProgram.py
The instructions for the program is in code. In python, a pound sign (#) is used to denote a comment. This is code that will not execute and is only there for the benefit of the programmer.

Please label all of your work. There is an area at the top of the code for the file name, your name, the purpose of the file, and the last revision date. Please update all of this info.
```
#FirstProgram.py
#Name:
#Date:
#Assignment: Lab 1
#Purpose: To ask a user for their name, and calculate their birth year.
```
- We are going to make a program that that says hello and asks for your name.  
- We have not yet used input, you will need the following code to make it work. Experiment to answer these questions.
  - Do I need a prompt or can I simply get input?
  - How do I use the value the user just gave me?
  - What is the data type of the value the user just gave me?
    - Can it be printed?
    - What happens if it is a number and we try to do math with it?
    - Can I convert data types if this one is not correct for my needs?

```
answer = input("This is a prompt for info: ")
print(answer)
```

## MadLib.py
Create a [Mad Lib](https://en.wikipedia.org/wiki/Mad_Libs) where the user supplies key adjectives, nouns, verbs, adverbs, or other types of speech then constructs a full story with those words.

Your Mad Lib must:
- Ask for at least 6 words
- Consider usability in design (be clear)
- Create a story with the user supplied words.

There are a few ways to join words in python:

```
noun1 = "Bicycle"
print("I like to ride my " + noun1)
print("I like to ride my", noun1)
```
Test which works best for you, note where the spaces fall using the different methods.

Please remember to fill in all of the info at the top of the document.


## Testing your code
You may not actually know that your code works until you fully test what you have written. It is often a good idea to get someone else to run your program, they may do something you had not anticipated which could show you a possible flaw or at least a design issue.

## End of class
In Repl.it, you will find the share link to your code. That is what gets submitted to Canvas.
