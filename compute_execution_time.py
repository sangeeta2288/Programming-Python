
# Let us use timeit module, which measures the execution time of small code snippet
#Start by importing timeit module

import timeit

# Compute the time required to create a list[1,2,3,4,5] over a million number of times
list_test = timeit.timeit(stmt="[1,2,3,4,5]", number = 1000000)
print(list_test)

# Compute the time required to create tuple(1,2,3,4,5) same over a million number of times
tuples_test = timeit.timeit(stmt="(1,2,3,4,5)", number = 1000000)
print(tuples_test)

# Hence we can conclude that, even though tuples are immutable they are fast in their operations. And also they consume less memory when comapred with Lists.
