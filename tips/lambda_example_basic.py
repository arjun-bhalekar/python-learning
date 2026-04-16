fruits = ['apple', 'banana', 'orange', 'mango', 'watermelon', 'pineapple']

# create another list having fruit name len > 5
fruits_more_than_5_len = list(filter(lambda x: len(x) > 5 , fruits))
print(fruits_more_than_5_len)

# create another list having fruit name start with 'a' OR 'o'
fruits_name_start_with_ovals = list(filter(lambda x: (str(x).startswith('a') | str(x).startswith('o')) , fruits))
print(fruits_name_start_with_ovals)

# map each object to diff object without filter
# convert each fruit name to uppercase and create new list
fruits_name_upper = list(map(lambda x: x.upper() , fruits))
print(fruits_name_upper)

numbers =list(range(11))
print(numbers)

numbers_square = list(map(lambda x: x ** 2, numbers))
print(numbers_square)