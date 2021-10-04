day=input("enter your day birthday: ")
mounth=input("enter your mounth birthday: ")
year=int(input("enter your year birthday: "))
yy=year%100
if 1<=int(day)<=31 and 1<=int(mounth)<=12 and 1950<=int(year)<=2020:
    if day[0]!="0":
        day="0"+ str(day)
    if mounth[0]!="0":
        mounth="0"+ str(mounth)
    print(f"{day}/{mounth}/{int(year%100)}")
else:
   print("error birthday")
