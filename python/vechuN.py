#for long nhau
"""
a = int(input("nhap a: "))
for x in range(a):
    for s in range(a):
        if s == 0 or x == s or x == a-1:
            print("*",end='')
        else: 
            print(" ",end=''
            )
    print("")
"""
"""
b = int(input("nhap b"))
x = 0
while x < b:
    s = 0
    while s < b:
        if s == 0 or x == s or x == b-1:
            print("#",end="")
        else:
            print(" ",end="")
        s +=1
    x +=1
    print()
    """
x = int(input("nhap x = "))
y = int(input("nhap y = "))
s = 0
i = 1
for i in range(1,y+1):
    tu = x**i
    mau = 1
    for j in range(1,i+1):
        mau = mau*j
    s = s + (tu/mau)
print("s({0},{1}) = {2}".format(x,y,s))        