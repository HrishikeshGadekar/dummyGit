# Input and Conditionals
if int(input("Enter 1st number: ")) > 10 and int(input("Enter 2nd number: ")) > 10:
    print('Both > 10')
else:
    print("Both < 10")

# ---
a, b, c = int(input("Enter 1st number: ")), int(input("Enter 2nd number: ")), int(input("Enter 3rd number: "))

if a >= b and a >= c:
    print(f"a = {a} is the greatest.")
elif b >= a and b >= c:
    print(f"b = {b} is the greatest.")
else:
    print(f"c = {c} is the greatest.")

# ---
l = [67, 12, 8, 6, 3, 2, 0, -2, -23]

for n in l:
    print(f"n = {n} :", end=' ')
    if n > 10:
        print("n > 10")
    elif 5 <= n <= 10:
        print("5 <= n <= 10")
    elif 0 < n < 5:
        print("0 < n < 5")
    else:
        print("n < 0")
