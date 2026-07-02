# implement number system
while True:
    print("\n===== Number System Conversion =====")
    print("1. Decimal to Binary")
    print("2. Decimal to Octal")
    print("3. Decimal to Hexadecimal")
    print("4. Binary to Decimal")
    print("5. Octal to Decimal")
    print("6. Hexadecimal to Decimal")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter Decimal Number: "))
        print("Binary =", bin(num)[2:])

    elif choice == 2:
        num = int(input("Enter Decimal Number: "))
        print("Octal =", oct(num)[2:])

    elif choice == 3:
        num = int(input("Enter Decimal Number: "))
        print("Hexadecimal =", hex(num)[2:].upper())

    elif choice == 4:
        num = input("Enter Binary Number: ")
        print("Decimal =", int(num, 2))

    elif choice == 5:
        num = input("Enter Octal Number: ")
        print("Decimal =", int(num, 8))

    elif choice == 6:
        num = input("Enter Hexadecimal Number: ")
        print("Decimal =", int(num, 16))

    elif choice == 7:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
