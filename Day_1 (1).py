# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 22:55:10 2026

@author: pavan
"""
print("Hello world!")

print("Hello",end=" ")

print("Harpal","Patel",sep="-")

print("My","Name","is",end="*")
print("Harpal","Patel",sep="-",end="*\n")

# check Number is Even or Odd 
n=int(input("Enter the value : "))
if n  % 2 == 0:
    print("Even")
else:
    print("Odd")

print(eval(input("perform operation : "))) #calculate directly

# Menu Driven Calculator
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

print("\n" + "*" * 10 + " MENU " + "*" * 10)
print("+  : Addition")
print("-  : Subtraction")
print("*  : Multiplication")
print("/  : Division")
print("%  : Modulus")
print("** : Power")
print("*" * 26)

choice = input("Enter your choice (+, -, *, /, %, **) : ")

if choice == "+":
    print("Addition =", num1 + num2)

elif choice == "-":
    print("Subtraction =", num1 - num2)

elif choice == "*":
    print("Multiplication =", num1 * num2)

elif choice == "/":
    if num2 != 0:
        print("Division =", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")

elif choice == "%":
    if num2 != 0:
        print("Modulus =", num1 % num2)
    else:
        print("Error: Modulus by zero is not allowed.")

elif choice == "**":
    print("Power =", num1 ** num2)

else:
    print("Invalid Choice! Please select a valid operator.")
    
# swap number without third variable 
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
print("Before Swapping \nNum1 :",num1," Num2 : ",num2)
num1,num2=num2,num1
        #or
num1=num1+num2
num2=num1-num2
num1=num1-num2
print("After Swapping \nNum1 : ",num1," Num2 : ",num2)
