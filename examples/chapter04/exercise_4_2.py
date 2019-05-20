count=0
numbers=set()# A set should be assigned before while here 
while True:
    data = input("Enter a number ( or the word 'end' to quit) :")
    if data =='end':# when meets the condition while loop breaks 
        break
    numbers.add(data)
print("the set is:",numbers)
list_numbers=sorted(numbers)
set_a=set(list_numbers)
#print(numbers.sort())
#print(count, "values were not unique")
print("the sorted set of line_numbers",list_numbers)
print("the sorted set of numbers",set_a)
print("lenght of numbers",len(set_a))
