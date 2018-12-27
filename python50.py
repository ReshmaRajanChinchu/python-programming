a=int(input("enter the no"))
for i in range(2,100):
    if(2**i==a):
        print(2,"^",i)
    else:
        print("not power of two")
