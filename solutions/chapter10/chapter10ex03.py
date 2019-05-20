#!/usr/bin/env python3
#
# A Solution For Chapter 10 Exercise 3
#
def fact(p):
	ans = p
	while ( p > 2 ):
		p -= 1
		ans *= p
	return ans

# dict of fact pairs

dictionary = dict ( [ (x, fact(x)) for x in range(1,11) ] )
print(dictionary)
print(dictionary[5] * dictionary[6])
