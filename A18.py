K=input("Enter the row:")
L=input("Enter the row:")
for i in range(K,L):
	n=0
	temp=i
	while temp>0:
		digit=temp%10
		n=n+digit ** 3
		temp/=10
	if i==n:
		print(i)
