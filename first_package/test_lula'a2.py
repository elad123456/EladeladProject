a=int(input("enter a number: "))
bool=False
i=2
while i<=9 and bool==False and i<a:
    if a%i==0:
        bool=True
    i+=1
if bool==False:
    print("מספר ראשוני")
else:
    if bool==True:
        print("מספר לא ראשוני")