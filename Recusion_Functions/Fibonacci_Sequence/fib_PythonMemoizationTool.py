
# GOAL: Write a function to return nth tern of fibonacci sequence

from functools import lru_cache

@lru_cache(maxsize=200)
def fibonacci(n):
	validate_input(n)
	if(n==1):
		return 1
	elif(n==2):
		return 2
	elif(n>2):
		return(fibonacci(n-1)+fibonacci(n-2))

def validate_input(n):
	if(type(n) != int):
		raise TypeError("n should be positive a integer")
	elif(n<1):
		raise ValueError("n should be a positive integer")

for n in range(1,101):
        print(n,":",fibonacci(n))

