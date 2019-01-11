s1,s2=input().split(' ')
a=0
b=0
if(len(s1)==len(s2)):
    for i in range(0,len(s1)-1,1):
        if(s1[i]==s1[i+1]):
            a=a+1
            print(a)
        if(s2[i]==s2[i+1]):
            b=b+1
        if(a!=b):
            print('no')
            break
    print(a>0,a,b)
    if a==b:print('yes')
else:print('no')

