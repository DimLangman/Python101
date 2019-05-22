number1 = int(input ("what is the first number?"))
operator = input("what do you want to do? + - * / or ** : ")
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
