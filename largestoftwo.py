# Python Program to find Largest of Two Numbers

a = float(input(" Please Enter the First Value a: "))
b = float(input(" Please Enter the Second Value b: "))

if(a - b > 0):
    print("{0} is Greater than {1}".format(a, b))
elif(b - a > 0):
    print("{0} is Greater than {1}".format(b, a))
else:
    print("Both a and b are Equal")
