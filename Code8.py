from random import randint
import easygui

question = easygui.ynbox(msg="Are you sure you want to continue?")

# q2 = easygui.multpasswordbox()

q3 = easygui.passwordbox()

q4 = easygui.choicebox(msg="Maak je keuze.", title="ABC", choices=("A", "B", "C"))

q5 = easygui.codebox(msg="Uitkomst.", title="RES", text=(q4))

q6 = easygui.diropenbox()

# print ("test")

print (q4)
