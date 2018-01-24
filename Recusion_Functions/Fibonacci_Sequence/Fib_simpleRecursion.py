
# GOAL: Write a function that returns Nth term of fibonacci sequence

def fibonacci(n):
	#Validate the input 
	validate(n)
	if (n==1):
		return 1
	elif (n==2):
		return 2
	elif (n>2):
		return (fibonacci(n-1) + fibonacci(n-2)) 

def validate(n):
	if(type(n) != int):
                raise TypeError("n must be positive integer")
	elif(n < 1):
		raise ValueError("n must be positive integer")

for n in range(1,11):
	print(n,":",fibonacci(n))

