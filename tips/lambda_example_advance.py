from functools import reduce

list_numbers = list(range(1, 11))
print(list_numbers)

# find sum of square of even numbers from list_numbers

print(
    reduce(lambda x, y: x + y,
           map(lambda x: x ** 2, list(filter(lambda x: x % 2 == 0, list_numbers)))
    )
)
