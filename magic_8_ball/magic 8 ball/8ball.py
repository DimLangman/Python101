from random import randint

import easygui

while True:
    question = easygui.enterbox(msg="Ask the magic 8 ball a question", image = "ball.gif")

    if question == None: break

    choice = randint(1,5)

    if choice == 1:
        text = "Concentrate and ask again"
        picture = "concentrate.gif"

    elif choice == 2:
        text = "Very doubtful"
        picture = "doubt.gif"

    elif choice == 3:
        text = "It's hazy"
        picture = "hazy.gif"

    elif choice == 4:
        text = "Yes"
        picture = "yes.gif"

    elif choice == 5:
        text = "No"
        picture = "no.gif"    

    easygui.msgbox(msg= text, image=picture)
