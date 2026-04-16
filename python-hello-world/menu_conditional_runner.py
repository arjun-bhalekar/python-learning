input1 = input("Enter number 1: ")
input2 = input("Enter number 2: ")
print("select operation :")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
print("5 - Exit")
choice = input("Enter your choice: ")

number1 = int(input1)
number2 = int(input2)

if choice == "1":
    print(f"{input1} + {input2} = {number1 + number2}")
elif choice == "2":
    print(f"{input1} - {input2} = {number1 - number2}")
elif choice == "3":
    print(f"{input1} * {input2} = {number1 * number2}")
elif choice == "4":
    print(f"{input1} / {input2} = {number1 / number2}")
elif choice == "5":
    exit()
else:
    print("wrong choice entered")
