def print_squares_of_numbers_upto(n):
    for i in range(1, n + 1):
        print('square of ' + str(i) + ' : ' + str(i * i))

def print_squares_of_even_numbers_upto(n):
    for i in range(2, n + 1, 2):
        # if i % 2 ==0:
            print('square of ' + str(i) + ' : ' + str(i * i))

def print_squares_of_odd_numbers_upto(n):
    for i in range(1, n + 1):
        if i % 2 == 1:
            print('square of ' + str(i) + ' : ' + str(i * i))

def print_numbers_in_reversed_order(n):
    for i in range(n, 0, -1):
        print(i)

def add_two_numbers(a, b):
    total = a + b
    return total


#print_squares_of_numbers_upto(10)
#print_squares_of_even_numbers_upto(10)
#print_squares_of_odd_numbers_upto(10)
#print_numbers_in_reversed_order(10)
print(add_two_numbers(5,6))