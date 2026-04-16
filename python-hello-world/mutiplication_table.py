def print_table_with_range(table=5, begin=1, end=10):
    print('--- printing table ---')
    for i in range(begin, end+1):
        #print(str(table) + " X " + str(i) + "= " + str(table * i))
        print(f"{table} X {i} = {table*i}")

# def print_table_five():
#     print_table_with_range(5,1,10)
#
# def print_table(table):
#     print_table_with_range(table,1,10)

# print_table_five()
# print_table(10)
print_table_with_range()
print_table_with_range(10)
print_table_with_range(2, 1, 20)
