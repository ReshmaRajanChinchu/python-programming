a=int(input("enter th:e n"))
b=[]
for i in range(0,a):
    c=int(input("enter the input"))
    b.append(c)
for i in range(0,a):
    if(b[i]!=i+1):
        print(i+1)
