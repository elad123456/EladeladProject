grade=int(input("enter a grade:"))
i=1
average=grade
sum=grade
max=grade
min=grade
while grade>=0 and grade<=100:
    print(max)
    print(average)
    print(max-min)
    grade = int(input("enter a grade:"))
    sum+=grade
    i+=1
    average=sum//i
    if grade>max:
        max=grade
    else:
        if grade<min:
            min=grade
