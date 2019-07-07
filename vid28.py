from random import randint
names = []
addingnames = True
while addingnames == True:
    newname = input("Please add a new name or press enter to pick a random one: ")
    if len(newname) > 0:
        names.append(newname)
    else:
        count = len(names)
        randomnr = randint(0,count-1)
        print (names)
        print ("En de selectie is geworden:")
        print (names[randomnr])
        addingnames = False
