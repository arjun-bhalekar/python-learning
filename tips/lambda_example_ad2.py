from functools import reduce

# input list
months = [('Jan', 31), ('Feb', 28), ('Mar', 31)]
print(months)

# 1. find the sum of days of all months
result = sum(map(lambda x : x[1], months))
print(result)

# 2. get month which have less no days - use reduce method
print(
    reduce(lambda x, y : x if x[1] < y[1] else y, months)
)
