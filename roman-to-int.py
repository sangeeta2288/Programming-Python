# GOAL: Comvert the given roman numeral into valid interger number
# Input range from 1-3999
# HINTS: I=>1 V=>5 X=>10, L=>50, C=>100, D=>500, M=>1000

class solution:
	def romantoint(self,s):
		dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
		value = 0
		for i in range(len(s)-1) :
			if(dict[s[i]] < dict[s[i+1]]):
				value = value - dict[s[i]]
			else:
				value = value + dict[s[i]]
		return value+dict[s[-1]]

my_sol = solution()
input = input("Enter a valid Roman Numeral: ")
result = my_sol.romantoint(input)
print(result)
