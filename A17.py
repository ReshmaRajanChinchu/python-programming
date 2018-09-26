n=int("Number:")
l=int("Number:")
x=0
for i in range(0,l):
    l=n[i]
    y=(int(l))**3
    x +=y
if x==int(n):
    print("amstrong no")
else:
    print("not an amstrong no")
