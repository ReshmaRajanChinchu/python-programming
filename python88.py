a=int(input("enter  no"))
b=int(input("enter  no"))
for i in range(1,(a*b)+1):
    if(i%a==0 and i%b==0):
      print(i)
      break
