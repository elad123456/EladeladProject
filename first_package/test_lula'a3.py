import random
bool=False
num=random.randrange(1, 9)
a=int(input("guess the number: "))
while bool==False:
    if a==num:
        bool=True
        print("congradulation!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        if a<num:
            print("bigger")
            a = int(input("guess the number: "))
        else:
            if a>num:
                print("smaller")
                a = int(input("guess the number: "))


