a=int(input("enter a number: "))
b=int(input("enter a number"))
if a<=b:
        while a<=b:
            if a%2==0:
                print(a)
            a+=1
else:
    if b<=a:
        while b<=a:
            if b%2==0:
                  print(b)
            b+=1