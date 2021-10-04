def rishoni(a):
    i=2
    while i<=9:
        if a%i==0:
            return False
        i+=1
    return True

i=1
ezer=111000000000000000000000000000000000000000000000000000000000000
while i<=5:
    num1 = int(input("enter a number:"))
    if rishoni(num1) and num1<ezer:
        ezer=num1
    i+=1
print(ezer)




