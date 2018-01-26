## Validate the given input contains valid pair of brackets.

class Solution:
	def isValid(self,s):
		mystack = []
		dict = {"}":"{","]":"[",")":"("}
		for item in s:
			if item in dict.values():
				mystack.append(item)
			elif item in dict.keys():
				if(mystack == [] or dict[item] != mystack.pop()):
					return False
			else:
				return False
		return mystack==[]		

solution = Solution()
input = input("Enter pattern==> ")
res = solution.isValid(input)
print(res)            
