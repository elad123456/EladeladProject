from random import randint
a=input("enter a number between 0-100: ")
i=0
num=randint(0, 100)
bool=False
big=100
small=0
bool2=True
while bool2==True:
    if a=='':
        print("you didnt enter a number")
        a = input("enter a number between 0-100: ")
    else:
        a=int(a)
        while bool!=True:
            bool2==False
            if a==num:
                bool=True
                print(f"congratulation,you took {i} guesess to guess my number!!!!!!!!!!!!!!!!!!")
            else:
                if num<a:
                    bool == False
                    small=num
                    num = int(randint(small, big))
                    i+=1
                else:
                    if num>a:
                        bool == False
                        big = num
                        num=int(randint(small, big))
                        i += 1
            print(num)
