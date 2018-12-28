a=input("Enter the input")
b="aAeEiIoOuU"
final = [each for each in a if each in b]
if len(final)>1:
    print("yes")
else:
    print("no")
