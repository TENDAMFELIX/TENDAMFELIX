#Membership Operators  : [ In / Not In ]
from re import X
from xxlimited import Str

from cupshelpers import Printer


List1 = [1,2,3,4,5,6]
if(1 in List1):
    print(1 , "Is Present in List")
if(7 not in List1):
    print(7, "Is Not Present In List")
    
List2 = ["Tirth" , "Shivam" , "Smit" , "Shiv" ]
if("Shivam" in List2):
    print("Shivam" , "Is Present in List2")
if("Vrutik" not in List1):
    print("Vrutik", "Is Not Present In List2")

Str1 = "TirthPatel"
if('T' in  Str1):
    print('T', "Is Present In String",Str1)

#Identitiy Operators : [Is / Is Not ]
Z = X
print("Z Is X",Z is X)

List3 = [1,2,3,4,5,6]
List4 = [1,2,3,4,5,6]
print("List3 Is List4",List3 is List4)
List4 = List3
print("List3 Is List4",List3 is List4)

#BitWise Operators
print("10 & 2 :",10 & 2)
print("10 | 2 :",10 | 2)
print("10 >> 2 :",10 >> 2)
print("10 ^ 2 :",10 ^ 2)

M = int(input())
K = M
SUM= 0
MUL = 1
while K > 0:
    SUM += K%10
    MUL*=K%10
    K=K//10
    
if(SUM+MUL == M):
    print("YES")
else:
    print("NO")

