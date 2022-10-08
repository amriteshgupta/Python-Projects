#To make calcultor
print("1.Addiion")
print("2.Subtraction")
print("3.Multiplicaton")
print("4.Division")
num1=float(input("enter the first number"))
num2=float(input("enter the second nmber"))
choice=int(input("enter a choice:-1,2,3,4"))
if choice==1:
    sum=num1+num2
    print(sum)
elif choice==2:
    sub=num1-num2
    print(sub)
elif choice==3:
    mul=num1*num2
    print(mul)
elif choice==4:
    div=num1/num2
    print(div)
else:
    print("Invalid choice")
    
