def rev(x):
	y=""
	index=len(x)
	while index>0 :
		y=y+str[ index - 1 ]
		index=index-1
	return y
print(rev("view"))
