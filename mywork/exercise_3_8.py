x=int(input("enter a number:"))
y=int(input("enter a number:"))
i=0
if x> y:
    x,y=y,x

for sum_range in range(x,y+1):
    i+=sum_range

print("value of sum of range is",i)
