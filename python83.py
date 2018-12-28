a=input("calculator")
try:
  k=a.split("/")
  print(int(k[0])/int(k[1]))
except:
    k = a.split("%")
    print(int(k[0])%int(k[1]))
