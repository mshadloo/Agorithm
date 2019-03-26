def swap(a,b):
    a=b-a
    b=b-a
    a=a+b
    return a,b
def swap2(a,b):
    a=a^b
    b=a^b
    a=a^b
    return a,b


print(swap2(40,60))
print(bin(40))
