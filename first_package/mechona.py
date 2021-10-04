def quantity(a):
    i=1
    sum = 0
    while a // (i * 10) != 0:
        i = i * 10
        sum += 1
    return sum+1

num=int(input("enter a number: "))
y=1
ezer=0
a=quantity(num)
while a>=y:
    if a!=y:
        ezer=ezer+((num%10)*(10**(a-y)))
    elif a==y:
        ezer = ezer + num % 10
    y+=1
    num=num//10
print(ezer)
print(ezer*2)


