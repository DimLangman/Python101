import datetime
import random

curtime = datetime.datetime(2019, 4, 27)
print (curtime)

rnd = random.Random()
rnd.seed(curtime.toordinal())

val = b'\xe3\x9c\x00\xa1\x1b">\xee\x15O\x13\xee*\xcb\xad]Y\xf4T\x85\x1e\xf1W3'
crypt = b""

for i in range(0,len(val)):
    r = rnd.randint(0,255)
    crypt += (val[i] ^ r).to_bytes(1,'big')


print(crypt)

print(int.from_bytes(b'\x00\x10', byteorder ='big'))

print(int.from_bytes(b'x88k|E\xa4\x9c\xc9\xfa\xb7~Jz\x00\x05tg\x90\xf8H\xeet\xdd\x80i', byteorder ='big'))

bystr = '\x88k|E\xa4\x9c\xc9\xfa\xb7~Jz\x00\x05tg\x90\xf8H\xeet\xdd\x80i'

print (bystr)

bad_bytes = b'\x02-\xdfI#)'
tex1 = str(bad_bytes)[2:-1]
print (tex1)
tex2 = str( bystr )[2:-1]
print (tex2)


str = bytes.decode(tex1)



str(bystr, 'utf-8', 'ignore')
print (bystr)



#/ str = bytes.decode(b'x88k|E\xa4\x9c\xc9\xfa\xb7~Jz\x00\x05tg\x90\xf8H\xeet\xdd\x80i')

#/ str = bytes.decode(bystr)

#/str(bystr, 'utf-8', 'ignore')
Print (bystr)




