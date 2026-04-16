def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


# print(is_prime(13))

def sum_upto(number):
    sum_value = 0
    for i in range(1, number+1):
        sum_value += i
    return sum_value

# print(sum_upto(5))

def print_triangle(number):
    for i in range(1, number+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()



print_triangle(10)