from random import randint

import easygui

while True:
    question = easygui.enterbox(msg="Ask the magic 8 ball a question", image = "ball.gif")

    if question == None: break

    choice = randint(1,2)

    if choice == 1:
        text = "Concentrate and ask again"
        picture = "concentrate.gif"

    elif choice == 2:
        text = "Very doubtful"
        picture = "doubt.gif"

    easygui.msgbox(msg= text, image=picture)
