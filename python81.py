k=int(input(""))
f=int(input(""))
flag=2**32
while k and f <flag:

   if(k-f<0):
      print(-1*(k-f))
   else:
       print(k-f)
   break
