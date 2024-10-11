import random as r
import string as s
strong=s.ascii_letters+s.digits+s.punctuation
medium=s.ascii_letters+s.digits
weak=s.ascii_letters
x='y'
print("......welcome to password generator application.....")
while x=='y':
    pas=""
    n=int(input("enter required length of password:"))
    pass_type=input("enter complexity of password ( strong (or) medium (or) (weak) ) :")
    if pass_type.lower()=='weak':
        for i in range(0,n):
            pas+=r.choice(weak)
        print(pas)
        x=input("choose (y/n) to generate another password:")
        if x.lower()=='n':
            print("thankyou for using password generator.......")
            break
    elif pass_type.lower()=='medium':
        for i in range(0,n):
            pas+=r.choice(medium)
        print(pas)
        x=input("choose (y/n) to generate another password:")
        if x.lower()=='n':
            print("thankyou for using password generator.......")
            break
    elif pass_type.lower()=='strong':
        for i in range(0,n):
            pas+=r.choice(strong)
        print(pas)
        x=input("choose (y/n) to generate another password:")
        if x.lower()=='n':
            print("thankyou for using password generator.......")
            break
    else:
        print("enter correct complexity")
        


