import random
lol = int(input("enter your account no."))
bal=5,00,000
max = 50,000
min = 500
zero = 0

pin = 98
ATMCARDNO = 99
if lol==ATMCARDNO:
    jj= int(input("enter pin  "))

elif lol!=ATMCARDNO:
    print("account doesnt exist  ")

if jj==pin:
    kk= int(input("welcome!"))

elif jj!=pin:
    print("Incorrect pin")

if input("balance"):
    print(bal)