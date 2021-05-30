import random
import string
import pyperclip

def passgenerator(platform,passlen,lower,upper,digit,special):

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
        print(platform," :- ",password)

    else:
        print("For secure password,Password length should be greater than or eqaul to 15.")

def passwordgenerator(pltf = 'Facebook',pl = 15,lw = 4,up = 3,dg = 5,sp = 3):
    if lw == 4 and up == 3 and dg == 5 and sp == 3:
            passgenerator(pltf,pl,lw,up,dg,sp)

    else:
        if pl == lw + up + dg + sp or pl > lw + up + dg + sp:
            passgenerator(pltf,pl,lw,up,dg,sp)

        else:
            print("password lenght should be greater than or equal to the sum of numbers of the different characters you want")  


