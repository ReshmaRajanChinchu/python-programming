c = input("Enter String: ")
if len(c) % 2 == 0:

   print(c[len(c) // 2 - 1] + c[len(c) // 2])
   k=c.replace( c[len(c) // 2 - 1],"*")
   print(k.replace(c[len(c) // 2 ],"*"))

else:

   print(c.replace(c[len(c) // 2],"*"))
