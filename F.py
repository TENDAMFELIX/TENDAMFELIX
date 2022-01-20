from unicodedata import name
from cupshelpers import Printer
from numpy import percentile
Name = input("Enter A Student Name : ")
RollNo = input("Enter A Student Roll Number : ")
Course1 = int(input("Enter Marks Of Course 1 : "))
Course2 = int(input("Enter Marks Of Course 2 : "))
Course3 = int(input("Enter Marks Of Course 3 : "))
Course4 = int(input("Enter Marks Of Course 4 : "))
Course5 = int(input("Enter Marks Of Course 5 : "))
Total_Marks = Course5+Course1+Course2+Course3+Course4
Percentage = float(Total_Marks*100 / 500)
print("\n")
print("----------------O  Student Report  O----------------")
print("Student Name : ", Name)
print("Student Roll Number : ", RollNo)
print("Student Percentage : ", Percentage)
if Percentage <= 100 and Percentage > 90:
    print("Student Grade : A+")
elif Percentage <= 90 and Percentage > 80:
    print("Student Grade : A")
elif Percentage <= 80 and Percentage > 70:
    print("Student Grade : B+")
elif Percentage <= 70 and Percentage > 60:
    print("Student Grade : B")
elif Percentage <= 60 and Percentage > 50:
    print("Student Grade : C+")
elif Percentage <= 50 and Percentage > 40:
    print("Student Grade : C")
else:
    print("Student Grade : ", "Fail")
