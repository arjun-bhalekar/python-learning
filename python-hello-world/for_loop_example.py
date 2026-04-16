
while True :
    string_input = input("Enter a String: ")
    print("1. Print each character")
    print("2. Print each word")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 3:
        exit()
    elif choice == 1:
        for ch in string_input:
            print(ch)
    elif choice == 2:
        for word in string_input.split():
            print(word)
    else :
        print("Wrong Choice")
        continue

