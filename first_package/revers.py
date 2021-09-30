Bnum=int(input("enter a number which include 3 digits: "))
a=Bnum%10
b=(Bnum%100-a)
c=(Bnum-a-b)/100
Lnum=a*100+b+c
print(int(Lnum))