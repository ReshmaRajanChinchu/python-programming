s1 = input("i")
words   = sum(c1.isalpha() for c1 in s1)
spaces  = sum(c1.isspace() for c1 in s1)
others  = len(s1) - words - spaces
print(others)

