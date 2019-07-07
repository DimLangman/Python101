import math
import time

def CalPI(precision):
    answer = round((math.pi),precision)
    return answer

precision=input('Enter number of digits you want after decimal:')

try:
    roundTo=int(precision)
    print (CalPI(roundTo))

except:
    print ("Error")

# nb_digits = 40
# print(format(math.pi, '.%dg' % nb_digits))

time.sleep(2)

print (math.pi)

time.sleep(2)

def make_pi():
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    for j in range(10000):
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2


my_array = []

for i in make_pi():
    my_array.append(str(i))
# print (my_array)

my_array = my_array[:1] + ['.'] + my_array[1:]
big_string = "".join(my_array)
print (big_string)
# print ("here is a big string:\n %s") % big_string 

time.sleep(4)

x, y, summing = 2, 3, 4

for count in range (0,100000000):
    summing *= (x/y)
    x += 2
    summing *= (x/y)
    y += 2
    print (summing)

