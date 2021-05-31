import random
import argparse
import string
import pyperclip

def passgenerator(website,passlen,lower,upper,digit,special):

    if passlen >= 15:
        c1 = string.ascii_uppercase
        c2 = string.ascii_lowercase
        c3 = string.digits
        c4 = string.punctuation

        s =[]

        s.extend(list(c1))
        s.extend(list(c2))
        s.extend(list(c3))
        s.extend(list(c4))

        random.shuffle(s)

        c =[]

        d1 = "".join(random.sample(c1, upper))
        d2 = "".join(random.sample(c2, lower))
        d3 = "".join(random.sample(c3, digit))
        d4 = "".join(random.sample(c4, special))

        c.extend(list(d1))
        c.extend(list(d2))
        c.extend(list(d3))
        c.extend(list(d4))

        random.shuffle(c)

        c.extend(list(s))

        ps = c[:passlen]

        password = "".join(ps)

        pyperclip.copy(password)
        print(website," :- ",password)

    else:
        return "For secure password,Password length should be greater than or eqaul to 15."




parser = argparse.ArgumentParser()
parser.add_argument('-pl','--passlen', type = int, help ="password length", default=15)
parser.add_argument('-w','--website', type = str, help = "website name", default='Facebook')
parser.add_argument('-lw','--lower', type = int, help = "Number of lower case characters", default=4)
parser.add_argument('-up','--upper', type = int, help = "Number of upper case characters", default=3)
parser.add_argument('-d','--digit', type = int, help = "Number of digits", default=5)
parser.add_argument('-s','--special', type = int, help = "Number of special characters", default=3)

args = parser.parse_args()

if __name__=='__main__':

    if args.lower == 4 and args.upper == 3 and args.digit == 5 and args.special == 3:
        passgenerator(args.website,args.passlen,args.lower,args.upper,args.digit,args.special)

    else:
        if args.passlen == args.lower + args.upper + args.digit + args.special or args.passlen > args.lower + args.upper + args.digit + args.special:
            passgenerator(args.website,args.passlen,args.lower,args.upper,args.digit,args.special)

        else:
            print("password lenght should be greater than or equal to the sum of numbers of the different characters you want")    
