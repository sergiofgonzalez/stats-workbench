def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}\n")


def sub(a, b):
    result = a - b
    print(f"{a} - {b} = {result}\n")


def mult(a, b):
    result = a * b
    print(f"{a} * {b} = {result}\n")


def div(a, b):
    quot = a // b
    rem = a % b
    print(f"{a} / {b} = {quot}; remainder = {rem}\n")


print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Integer Division")
print("E. Exit")

while True:
    choice = input("Type your option: ")
    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("Enter first number: "))
        b = int(input("Second number: "))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("Enter first number: "))
        b = int(input("Second number: "))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("Enter first number: "))
        b = int(input("Second number: "))
        mult(a, b)
    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("Enter first number: "))
        b = int(input("Second number: "))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("Exit")
        quit()
