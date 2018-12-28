a=int(input("enter  no"))
b=int(input("enter  no"))
for i in range(b,0,-1):
    if(a%i==0 and b%i==0):
      print(i)
      break

