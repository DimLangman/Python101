from random import randint

# Function definition is here
def printme(strng):
# "This prints a passed string into this function"
  print (strng)
  return

# Now you can call printme function
printme(strng = "My string");

# Function definition is here
def guessme():
# "This tests guess function"
  attemptnumb1 = 0
  randnumb1 = randint(1,10)
  guesscorrect = False
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

# Now you can call guessme function
guessme(); 

# Function definition is here
def basicmath(letsgo):
  while letsgo == True:
    operator = input("what do you want to do? + - * / ** or q(quit): ")
    if operator =="q":
      letsgo = False
    else:
      number1 = int(input ("what is the first number?"))
      number2 = int(input ("what is the second number?"))
      if operator =="+": 
        answer = number1 + number2
      elif operator =="-":
        answer = number1 - number2
      elif operator =="*":
        answer = number1 * number2
      elif operator =="/":
        answer = number1 / number2
      elif operator =="**":
        answer = number1 ** number2
      else:
        print("Wrong operator!!")
        answer = "Omega"
      print("the answer is " + str(answer))
    return

# Now you can call basicmath function
basicmath(letsgo = True); 
