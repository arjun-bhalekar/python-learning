# A list comprehension is a concise, one-line way to create a new list in Python by applying an operation to each item in an existing list or range.
# It is often used as a cleaner alternative to a traditional for loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

# creating new list with square of each n from existing list
squares = [n**2 for n in numbers]
print(squares)

# filtering only even numbers
even_numbers = [n for n in numbers if n%2 == 0]
print(even_numbers)

# filtering only even numbers
odd_numbers = [n for n in numbers if n%2 != 0]
print(odd_numbers)

