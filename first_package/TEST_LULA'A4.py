import random
a=int(input("enter a number between 0-100: "))
i=0
num=random.randrange(0, 100)
bool=False
big=100
small=0
while bool!=True:
    if a==num:
        bool=True
        print(f"congratulation,you took {i} guesess to guess my number!!!!!!!!!!!!!!!!!!")
    else:
        if num<a:
            bool == False
            small=num
            num = int(random.randrange(small, big))
            i+=1
        else:
            if num>a:
                bool == False
                big = num
                num=int(random.randrange(small, big))
                i += 1
    print(num)
