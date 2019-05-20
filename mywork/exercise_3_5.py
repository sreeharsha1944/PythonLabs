x=int(input("enter a number:"))
y=str(x)
n=int(input("enter the split by value for the above integer:"))
out = [(y[i:i+n]) for i in range(0, len(y), n)] 

print(out)

for number in out:
    number = int(number)
    if number > 0:
        print(number, end=";")
print()
