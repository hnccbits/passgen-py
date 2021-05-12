import random
import argparse
import sys
import string

def passgenerator(args):
    c1 = string.ascii_uppercase
    c2 = string.ascii_lowercase
    c3 = string.digits
    c4 = string.punctuation

    s =[]
    
    s.extend(list(c1))
    s.extend(list(c2))
    s.extend(list(c3))
    s.extend(list(c4))

    password = "".join(random.sample(s, args.l))
    return password

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--l' , type=int, default=15, help ="This is a utility to give a password of the length you want")

    args = parser.parse_args()
    sys.stdout.write(str(passgenerator(args)))

