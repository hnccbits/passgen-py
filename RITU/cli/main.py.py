import random
import argparse
import os
import array
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import pyperclip

max_lenght=12

t1=digits
t2=ascii_uppercase
t3=ascii_lowercase
t4=punctuation

combined_list=digits+ascii_uppercase+ascii_lowercase+punctuation

rand_digits=random.choice(digits)
rand_upper=random.choice(ascii_uppercase)
rand_lower=random.choice(ascii_lowercase)
rand_punctuation=random.choice(punctuation)

temp_pass=rand_digits+rand_upper+rand_lower+rand_punctuation

temp_pass=temp_pass+random.choice(combined_list)
temp_pass_list=array.array('u',temp_pass)
random.shuffle(temp_pass_list)
password=""
for x in temp_pass_list:
    password=password+x


password="".join(temp_pass)
print(password)


print (password)
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
















