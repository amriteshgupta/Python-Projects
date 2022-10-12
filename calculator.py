# To make calcultor
print("1.Addiion")
print("2.Subtraction")
print("3.Multiplicaton")
print("4.Division")
valid = False
while not valid:
    try:
        num1 = float(input("Enter the first number"))
        valid = True
    except ValueError:
        print('Input not valid, please retry')
valid = False
while not valid:
    try:
        num2 = float(input("Enter the second number"))
        valid = True
    except ValueError:
        print('Input not valid, please retry')

valid = False
while not valid:
    choice = int(input("Enter a choice: 1,2,3,4"))
    if choice not in [1,2,3,4]:
        print("Invalid choice, please retry")
    else:
        valid = True

if choice == 1:
    sum = num1 + num2
    print(sum)
elif choice == 2:
    sub = num1 - num2
    print(sub)
elif choice == 3:
    mul = num1 * num2
    print(mul)
elif choice == 4:
    div = num1 / num2
    print(div)
