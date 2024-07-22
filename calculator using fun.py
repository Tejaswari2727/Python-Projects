def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
option=int(input("enter the option:"))
print('''
       1.Addition
       2.Sutraction
       3.Multiplication
       4.Division
       ''')
a=int(input("enter the first value:"))
b=int(input("enter the second value:"))
if option==1:
   print("Addition:",a+b)
elif option==2:
    print("Subtraction:",a-b)
elif option==3:
    print("Multiplication:",a*b)
elif option==4:
    print("Division:",a/b)
else:
    print("not valid")

