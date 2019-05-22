from random import randint

randnumb1 = randint(1,10)
guesscorrect = False
attemptnumb2 = 0

while guesscorrect == False:
    guess = int(input("What is your guess? "))
    attemptnumb2 += 1
    if (randnumb1) == (guess):
        guesscorrect = True
        print ("Well done, you got it right. The correct number was " + str(guess))
        print ("You took " + str(attemptnumb2) + " guesses." )
    elif (guess) < (randnumb1):
        print ("Guess higher!")
    elif (guess) > (randnumb1):
        print ("Guess lower!")
    else:
        print ("Unlucky, error detected. Wrong input?")
        
                  
