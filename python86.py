a=input("enter input")
flag=0
for i in range(0,len(a)):
    if(a.count(a[i])>1):
        flag=flag+1
if(flag==0):
    print("yes")
else:
    print("no")
