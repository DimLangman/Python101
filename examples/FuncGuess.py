from random import randint

# Function definition is here
def printme(strng):
# "This prints a passed string into this function"
  print (strng)
  return

# Now you can call printme function
printme(strng = "My string");

# Function definition is here
def guessme(guesscorrect):
# "This tests guess function"
  attemptnumb1 = 0
  randnumb1 = randint(1,10)
  while guesscorrect == False:
    guess = int(input("What is your guess? "))
    attemptnumb1 += 1
    if (randnumb1) == (guess):
        guesscorrect = True
        print ("Well done, you got it right. The correct number was " + str(guess))
        print ("You took " + str(attemptnumb1) + " guesses." )
    elif (guess) < (randnumb1):
        print ("Guess higher!")
    elif (guess) > (randnumb1):
        print ("Guess lower!")
    else:
        print ("Unlucky, error detected. Wrong input?")
  return

# Now you can call printme function
guessme(guesscorrect = False); 
  
  
