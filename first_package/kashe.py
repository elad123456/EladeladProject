def maximum(a):
    i=0
    max=-1
    while len(a)>=i:
        if(max<a[i]):
            max=a[i]
        i+=1
    return max
def minimum(a):
    i=0
    min=100000000000000000000000000000000000000000000000000000000000000000
    while len(a)>=i:
        if(min<a[i]):
            min=a[i]
        i+=1
    return min

numbers=list(range(10))
print(int(maximum(numbers)))
print(int(minimum(numbers)))

