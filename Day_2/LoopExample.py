
#print 3 to 19 in sequence with jump 2.
for i in range(3,20,2):
    print(i,end=" ")
    
print("\n")

#print -10 to -1
for i in range(-10,0):
    print(i,end=" ")

print("\n")

#break
print("Break : ",end="")
for i in range(1, 11):
    if i == 6:
        break
    print(i,end=" ")
    
print("\n")

#continue
print("Continue : ",end="")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i,end=" ")
    
print("\n")

#pass
print("Pass : ",end="")
for i in range(1, 6):
    if i == 3:
        pass
    print(i,end=" ")
    
print("\n")

# while loop menu driven
while True:
    print("*"*5,"Ticket Counter","*"*5)
    print("1. Calculate Ticket Price")
    print("2. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        age = int(input("Enter your age: "))

        if age < 5:
            print("Ticket Price: Free")
        elif age <= 17:
            print("Ticket Price: ₹10")
        elif age <= 64:
            print("Ticket Price: ₹20")
        else:
            print("Ticket Price: ₹12")

    elif choice == 2:
        print("Thank you!")
        break

    else:
        print("Invalid Choice!")
print("\n")

#print fibonacci serices for n numbers
def fibonacci(n):
    a=0
    b=1
    print("Fibonacci serices : ",end="")
    for i in range(n):
        print(a,end=" ")
        c=a+b
        a=b
        b=c
fibonacci(10)

print("\n")

#find factorial
def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)
print("Factorial : ",factorial(5))
