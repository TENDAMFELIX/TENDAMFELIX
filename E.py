Num1 = int(input("Enter A Integer Number : "))
Sum = 0
Mul = 1
Temp = Num1
while Temp > 0:
    Sum += Temp%10
    Mul *= Temp%10
    Temp //= 10

if (Sum+Mul) == Num1:
    print(Num1," Is Special Number")
else:
    print(Num1," Is Not Special Number")