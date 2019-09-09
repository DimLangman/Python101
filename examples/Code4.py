import time
print (" ")
print ("*********************")
print ("SYSTEM SENTINAL")
time.sleep(0.2)
print ("BIOS 7.205")
time.sleep(0.2)
print ("FW ENABLED / TRACE ON")
time.sleep(0.8)
print ("Boot SEQ 005")
print ("*********************")
print (" ")
time.sleep(1)
print ("C:\> RUN PROGRAM BlackFox.exe")
time.sleep(0.6)
print (" ")
time.sleep(0.6)

inputid = input("Enter ID: ")
print ("Verifying access for " + inputid)
import time

for x in range(0, 20) :
        print (".", end='')
        time.sleep(0.2)
print (" ")

if inputid == "p1lgr1m" :
    print("Welcome")
elif inputid == "root" :
    inputww = input("Enter password: ")
    for x in range(0, 20) :
        print (".", end='')
        time.sleep(0.2)
else :
    print("Invalid ID")

