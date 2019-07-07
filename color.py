# Python program to print 
# red text with green background 

import colorama
from colorama import init
init(strip=False)

from colorama import Fore, Back, Style 
print(Fore.RED + 'some red text') 
print(Back.GREEN + 'and with a green background') 
print(Style.DIM + 'and in dim text') 
print(Style.RESET_ALL) 
print('back to normal now') 


# C:\Users\D1m\AppData\Local\Programs\Python\Python37
# C:\Users\D1m\CloudStation\Development



# from colorama import init
# from termcolor import colored

# use Colorama to make Termcolor work on Windows too
# init()

# then use Termcolor for all colored text output
# print(colored('Hello, World!', 'blue'))
