x=input("enter a number:")
if not x.isnumeric():
    print("Number entered is not an integer")
else:
    print(x, 'is', len(x),'digits in length' )

