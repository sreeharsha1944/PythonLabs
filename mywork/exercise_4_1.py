count=0
numbers=set()# A set should be assigned before while here 
while True:
    data = input("Enter a number ( or the word 'end' to quit) :")
    if data =='end':# when meets the condition while loop breaks 
        break
    if data in numbers:#when data exists then do a counter
        count+=1
    else:
        numbers.add(data)#when data does not already exist add it to list
print("the set is:",numbers)#print conditions should be out of the "if" to get 
#data as an output in one go at the end of the break
print(count, "values were not unique")
