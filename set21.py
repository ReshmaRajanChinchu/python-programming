def nnum( a, d, n):
	num = 0
	i  = 0
	while( i < n ):
		num = num + a
		a = a + d
		i = i + 1
            return(num)
a = 3
d = 5
n = 8
print(nnum( a, d, n))

