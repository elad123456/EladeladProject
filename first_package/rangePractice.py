a=int(input("enter a number: "))
digit=a%10
asarot=a//10%10
meot=a//100
if 100<=a<=1000:
        if digit>=asarot and digit>=meot:
            print(digit)
        elif asarot>=digit and asarot>=meot:
                print(asarot)
        elif meot>=digit and meot>=asarot:
                    print(meot)

