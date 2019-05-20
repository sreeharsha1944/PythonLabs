#!/usr/bin/env python3
# conversions to an integer
result = input("Please enter an integer: ")
number = int(result)
print("Your number plus 10 equals:", number + 10)
print("String of", result, "converted to various bases as int:")
print("Base 10:", int(result), "\tBase 2:", int(result, 2))
print("Base 8:", int(result, 8), "\tBase 16:", int(result, 16))

# conversions to a float
a_float = input("Please enter a decimal number: ")
sum_of_input = float(a_float) + float(result)
print(a_float, "+", result, "=", sum_of_input)

print(number, "as string in the following bases:")
print("Binary:", bin(number))
print(" Octal:", oct(number))
print("   Hex:", hex(number))

print('ord("A") =', ord("A"), '     chr(66) =', chr(66))

the_sum = "The sum of the input equals " + str(sum_of_input)
print(the_sum)
