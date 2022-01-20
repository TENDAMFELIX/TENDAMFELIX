a = "Tirth Patel"
# Center
print(a.center(50))
# Left
print(a.ljust(50, " "))
# Right
print(a.rjust(50, " "))

print("{:>40}".format("Hello World"))

print("{:^140}".format("Hello World"))

# Zero Fill
b = '+15'
c = '-15'
print(b.zfill(5))
print(c.zfill(5))

a = 5
b = 2

print("a={0:d} and b={1:d}".format(a, b))
print("a={0:3d} and b={1:5d}".format(a, b))
print("a={0:>3d} and b={1:>5d}".format(a, b))
print("a={0:<3d} and b={1:<5d}".format(a, b))
print("a={0:03d} and b={1:05d}".format(a, b))
print("a={0:^3d} and b={1:^5d}".format(a, b))
print("a={:f}".format(123.456789))
print("a={:8.3f}".format(123.456789))
# (ii)
# Before Changing

x = 10
y = x
print("\nBefore Changing")
print("Value of x:", x)
print("Value of y:", y)
print("Id of x:", id(x))
print("Id of y:", id(y))

x = x + 1

print("\nAfter Changing")
print("Value of x:", x)
print("Value of y:", y)
print("Id of x:", id(x))
print("Id of y:", id(y))

m = list([1, 2, 3, 4])
n = m
print("\nBefore Changing")
print("List m:", m)
print("List n:", n)
print("Id of m:", id(m))
print("Id of n:", id(n))

m.pop()

print("\nAfter Changing")
print("List m:", m)
print("List n:", n)
print("Id of m:", id(m))
print("Id of n:", id(n))