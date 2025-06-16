def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Can't divide by 0"
    return x / y

print("Select operation:")
print("1.Add 2.Subtract 3.Multiply 4.Divide")

choice = input("Enter choice (1/2/3/4): ")
a = float(input("First number: "))
b = float(input("Second number: "))

if choice == '1':
    print(add(a, b))
elif choice == '2':
    print(subtract(a, b))
elif choice == '3':
    print(multiply(a, b))
elif choice == '4':
    print(divide(a, b))
else:
    print("Invalid input")
