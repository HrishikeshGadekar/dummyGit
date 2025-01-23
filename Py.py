# Input and Conditionals
if int(input("Enter 1st number: ")) > 10 and int(input("Enter 2nd number: ")) > 10:
    print('Both > 10')
else:
    print("Both < 10")

a, b, c = int(input("Enter 1st number: ")), int(input("Enter 2nd number: ")), int(input("Enter 3rd number: "))

if a >= b and a >= c:
    print(f"a = {a} is the greatest.")
elif b >= a and b >= c:
    print(f"b = {b} is the greatest.")
else:
    print(f"c = {c} is the greatest.")
