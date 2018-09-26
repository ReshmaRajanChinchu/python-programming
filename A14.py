s=int("s=")
e=int("e=")
if(s<=100000) & (e<=100000):
	for x in range(s,e+1):
	if(x%2!=0):
	print(x)
else:
	print("Input is invalid")
