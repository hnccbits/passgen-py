import random
import argparse
import os
import sys
import string

print('hello,welcome to password generator!')
slen=int(input('enter the length of password'))
letters=string.ascii_letters
num=string.digits
symbol=string.punctuation

my=letters+num+symbol
temp=random.sample(my,slen)
password="".join(temp)
print(password)


my_parser=argparse.ArgumentParser(description='list the content of a folder')
my_parser.add_argument('path',metavar='path',type=str,help='the path to list')
args=my_parser.parse_args()

input_path=args.path
if not os.path.isdir(input_path):
    print('the path specified does not exist')
    sys.exit()
print('\n'.join(os.listdir(input_path)))