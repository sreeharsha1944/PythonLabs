prompt = "Enter a number (or the word 'end' to quit):"
count=0
number=set()
while True:
    data = input(prompt)
    if data=="end":
        break
    if data in number:
        count=count+1
    else:
        number.add(data)
	
print("My Set data is:",number)
print("Number of duplicates passed in input is:",count)