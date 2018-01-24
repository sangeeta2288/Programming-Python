
""" Let us use timeit module, which measures the execution time of small code snippet"""

import timeit

# Compute the time required to create a list[1,2,3,4,5] over a million number of times
list_test = timeit.timeit(stmt="[1,2,3,4,5]", number = 1000000)
print(list_test)
