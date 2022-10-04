# BMI Calculator
# Enter your Height and Weight to Find your BMI

Height = input("Enter height in cm: ")
Weight = input("Enter weight in kg: ")
try:
    Height = float(Height)
    Weight= float(Weight)
    Height = Height / 100
    BMI = Weight / (Height * Height)
    print("your BMI is: ", BMI)
    if BMI > 0:
        if BMI <= 16:
            print("you are severely underweight")
        elif BMI <= 18.5:
            print("you are underweight")
        elif BMI <= 25:
            print("you are Healthy")
        elif BMI <= 30:
            print("you are overweight")
        else:
            print("you are severely overweight")
    else:
        ("Details are Wrong")
except ValueError:
    print("The Provided Value is not a number:")
    exit()