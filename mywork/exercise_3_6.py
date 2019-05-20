x=int(input("enter value of lower limit number:"))
y=int(input("enter value of higher limit number:"))
z=int(input("enter value of z a step value:"))

i=0
for sum_value in range (x,y+1,z):
    i+=sum_value
    
print('Total value of sum in range is:',i)

