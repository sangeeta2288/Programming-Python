
# GOAL : Inorder to improve the performace of recursion functions, we can use Python's Memoization concept
# Explicitly implement the concept of Memoization (using Dictionary in this prog)

fib_cache = {}
def fibonacci(n):
	validate_input(n)
	#check: if we have cached value of nth term, if so simply return it
	if n in fib_cache:
		return fib_cache[n]

	#Compute fib of nth term
	if (n == 1):
		return 1
	elif(n == 2):
		return 2
	elif(n > 2):
		value = fibonacci(n-1)+fibonacci(n-2)
		# Save the nth term value in fib_cache for subsequent use. And then return the computed value
		fib_cache[n]= value
		return value

def validate_input(n):
	if(type(n) != int):
		raise TypeError("n should be positive a integer")
	elif(n<1):
		raise ValueError("n should be a positive integer")

for n in range(1, 101):
	print(n,":",fibonacci(n))
