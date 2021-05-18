import random
import argparse
import os
import sys
import string
import pyperclip

print('hello,welcome to password generator!')
slen=int(input('enter the length of password'))
letters=string.ascii_letters
num=string.digits
symbol=string.punctuation

my=letters+num+symbol
temp=random.sample(my,slen)
password="".join(temp)
print(password)

pyperclip.copy('password')
print(pyperclip.paste())

if __name__=='__main__':



     my_parser=argparse.ArgumentParser(description="password generator")
     my_parser.add_argument('-sl','--slen',type=int, help="password length",default=20)
     my_parser.add_argument('-l','--letter',type=str, help="lower and upper case characters",default=8)
     my_parser.add_argument('-d','--digits',type=int, help="digits",default=6)
     my_parser.add_argument('-p','--punctuation',type=int, help="punctuation",default=3)

     args=my_parser.parse_args()
     print(args.slen,args.letter,args.digits,args.punctuation)


