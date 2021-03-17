first_value = int(input("Enter the first value: "))

second_value= int(input("Enter the second value: "))

operation = input("Please choose the right arithmetic operation (+, -, *, /): ")

if operation == "+":
    print(first_value + second_value)
elif operation == "-":
    print(first_value - second_value)
elif operation == "*":
    print(first_value * second_value)
elif operation == "/":
    print(first_value / second_value)
else:
    print("You did not provide the correct values for operation.")
