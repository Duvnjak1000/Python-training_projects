first_value = int(input("Enter the first value: "))

second_value= int(input("Enter the second value: "))

operation = input("Please choose the right arithmetic operation (+, -, *, /): ")

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)
else:
    print("You did not provide the correct values for operation.")
