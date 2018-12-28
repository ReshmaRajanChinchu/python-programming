num=input("Enter your Roman:")
st=list(num)
a1=[]
for x in st:
	if x=="V" or x=="v":
		a1.append(5)
	elif x=="I" or x=='i':
		a1.append(1)
	elif x=="X" or x=='x':
		a1.append(10)
	elif x=="L" or x=='l':
		a1.append(50)
	elif x=="C" or x=='c':
		a1.append(100)
	elif x=="D" or x=='d':
		a1.append(500)
	elif x=="M" or x=='m':
		a1.append(1000)
 
k=a1.index(max(a1))
ans=max(a1)
if k==0:
	for x in range(1,len(a1)):
		ans=ans+a1[x]
else:
	for x in range(len(a1)-1):
		ans=ans-a1[x]
print(ans)

