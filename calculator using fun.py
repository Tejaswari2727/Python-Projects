print('''
       1.Addition
       2.Sutraction
       3.Multiplication
       4.Division
       ''')
option=int(input("enter the option:"))
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

