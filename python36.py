n = input("i")
numbers = sum(c.isdigit() for c in n)
words   = sum(c.isalpha() for c in n)
spaces  = sum(c.isspace() for c in n)
specialcharacter  = len(n) - numbers - words - spaces
print(specialcharacter)
