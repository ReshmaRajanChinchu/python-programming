try:
	m1=int(input())
	m2=int(input())
	while(m2!=0):
		t=m2
		m2=m1%m2
		m1=t
	print(m1)
except:
	print('invalid')
