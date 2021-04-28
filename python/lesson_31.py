#hoc for else
a = int(input("nhap so nguyen: "))
s = 0
for x in range(5,10):
    if 4 % a == 1:
        print("stop for")
        break
    s = s + x
else:
    print("sum = ",s)