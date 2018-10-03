num=input("Enter the value:")
f=input("Enter the value:")
if(num<0):
	print('not a factorial number')
elif(num==0):
	print('factorial')
else:
	for x in range(1,num+1):
		f=x*f
print(f)
