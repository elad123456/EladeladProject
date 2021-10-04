age=int(input("enter your age: "))
if 0<=age<=18:
    print("child")
else:
    if 19 <= age <= 60:
        print("adult")
    else:
        if age>60:
              print("senior")