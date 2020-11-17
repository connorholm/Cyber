#BasicEnigma.py
#Name:
#Date:
#Assignment:

#This is a simplified version of the German Enigma used during WWII.

def translate(startLetters, endLetters, spot):
    #find the letter at (spot) in the startLetters string.
    #find the location of the letter in the endLetters string.
    index = 0
    for letter in endLetters:
        if letter == startLetters[spot]:
            return index
        index =+ 1
    return -1



def rotate(alphabet):
    letters = []
    #move the first letter of the alphabet to the end
    #shift all the letters
    index = 0
    newAlphabet = ""
    for letter in alphabet:
        if index > 0 and index < 25:
            letters.append(letter)
        if index == 25:
            letters.append(letter)
        index =+ 1
    letters.append(alphabet[:1])
    for letter in letters:
        newAlphabet = newAlphabet+letter
    return newAlphabet #this has been rotated


def main():
    alpha =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    #rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    #rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    reflectorA = "EJMZALYXVBWFCRQUONTSPIKHGD"

    # get a message from the user

    message = "HELLO"
    letter = message[0]

    # Find location of letter in alphabet
    pos = alpha.find(letter)

    #pass this letter through rotor1
    pos = translate(alpha, rotor1, pos) #starting, ending, current position
    
    print(translate(alpha, rotor1, pos))
    
    #Reflector
    pos = translate(alpha, reflectorA, pos)

    ### Now go back through in the reverse order

    pos = translate(rotor1, alpha, pos)

    #Translate back from position to a letter
    letter = alpha[pos]

    # Now that we have been through one pass, adjust any of the rotors that need to be rotated.
    rotor1 = rotate(rotor1)

    
    print(letter) #This one letter has been encoded


main()
