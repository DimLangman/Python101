import datetime
import random

curtime = datetime.datetime(2019, 5, 23)
print (curtime)

rnd = random.Random()
rnd.seed(curtime.toordinal())

val = b'\xe3\x9c\x00\xa1\x1b">\xee\x15O\x13\xee*\xcb\xad]Y\xf4T\x85\x1e\xf1W3'
crypt = b""

for i in range(0,len(val)):
    r = rnd.randint(0,255)
    crypt += (val[i] ^ r).to_bytes(1,'big')

print(crypt)





