a=input("enter the first num:")
b=input("enter the SOCOND num:")
bool=True
while bool==True:
    if a=='':
        a = input("enter the first num:")
    else:
        if b=='':
                    b = input("enter the SOCOND num:")
        else:
            if a!='' and b!='':
                bool=False
a=int(a)
b=int(b)
if a<=b:
 while a<=b:
    if a%3==0 and a%5==0:
        print("fizbaz")
    else:
        if a%3==0:
            print("fiz")
        else:
            if a%5==0:
                print("baz")
            else:
                print(int(a))
    a += 1
else:
        while b <= a:
            if b % 3 == 0 and b % 5 == 0:
                print("fizbaz")
            else:
                if b % 3 == 0:
                    print("fiz")
                else:
                    if b % 5 == 0:
                        print("baz")
                    else:
                        print(int(b))
            b += 1