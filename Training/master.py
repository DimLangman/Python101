import time
import random # voorheen from random import randint
import socket # nodig voor IP adres in Intro
import base64  # nodig voor encode en decode Base 64
# import easygui  # later nodig voor GUI

# Intro
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
print ("C:\> RUN PROGRAM BlackFox.exe on")
print (socket.gethostbyname(socket.gethostname()))
time.sleep(0.6)
print (" ")
time.sleep(0.6)

# // Login
inputid = input("Enter ID: ")
print ("Verifying access for " + inputid)
for x in range(0, 20) :
        print (".", end='')
        time.sleep(0.2)
print (" ")

# // Check login
if inputid == "p1lgr1m" :
    print("Welcome")
elif inputid == "root" :
    inputww = input("Enter password: ")
    for x in range(0, 20) :
        print (".", end='')
        time.sleep(0.2)
else :
    print("Invalid ID")
print (" ")
	
# // Voorbeeld dictionary	
print ("Voorbeeld dictionary")
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print (" ")
print (dict['one']) # Prints value for 'one' key
print (dict)
print (dict['one']) # Prints value for 'one' key
print (dict[2]) # Prints value for 2 key
print (tinydict) # Prints complete dictionary
print (tinydict.keys()) # Prints all the keys
print (tinydict.values()) # Prints all the values 


# Voorbeeld decode IT dag
import datetime
# import random
curtime = datetime.datetime(2019, 5, 23)
print (" ")
print ("Voorbeeld IT dag")
print (curtime)
rnd = random.Random()
rnd.seed(curtime.toordinal())
val = b'\xe3\x9c\x00\xa1\x1b">\xee\x15O\x13\xee*\xcb\xad]Y\xf4T\x85\x1e\xf1W3'
crypt = b""
for i in range(0,len(val)):
    r = rnd.randint(0,255)
    crypt += (val[i] ^ r).to_bytes(1,'big')
showval = len(val)
print(showval)
print(crypt)
print (" ")

# import base64
print ("Voorbeeld encode Base 64")
inputtxt = input("Enter text: ")
print (inputtxt)
print("Encoded text with base 64 is: ")
data1 = base64.b64encode(inputtxt.encode())
print(data1)

print("Decoded text with base 64 is: ")
data2 = base64.b64decode(data1).decode('utf-8')
print(data2)

print (" ")
print ("WW in B64 ")
data3 = base64.b64decode(b'NzJ0Z25ncGxncm0=').decode('utf-8')
print (data3)
print (" ")

	
