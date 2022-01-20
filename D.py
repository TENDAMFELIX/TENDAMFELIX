from ast import Num


Num1 = int(input("Enter A Integer Number : "))
Num2 = int(input("Enter A Integer Number : "))
Operator = input("Enter a operation [ + , - , * , / ] : ");
print("Value Of ",Num1,Operator,Num2," Is : ",end="")
if Operator == '+':
    print(Num1+Num2)
elif Operator == '-':
    print(Num1-Num2)
elif Operator == '*':
    print(Num1*Num2)
else :
    print(Num1/Num2)
