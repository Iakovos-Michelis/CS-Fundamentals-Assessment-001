a = int(input("Enter the starting point (a): "))
b = int(input("Enter the ending point (b): "))
c = int(input("Enter the step (c): "))

if a < b:
    for i in range(a, b+1, c):
        print(i, end=", ")
else:
    for i in range(a, b-1, -c):
        print(i, end=", ")