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
        if n%2 == 0:
            print("Even", end=' ')
        print("n > 10")
    elif n >= 5:
        print("5 <= n <= 10")
    elif n > 0:
        print("0 < n < 5")
    else:
        print("n < 0")

# while loop
n = int(input())
rev_n = 0

while n > 0:
    rev_n = rev_n*10 + n%10
    n //= 10
    
print(f"Revered n = {n} is {rev_n}")

# Prime check
n = int(input("Enter a number: "))
limit = int(pow(n, 0.5))

for i in range(2, limit + 1):
    if n%i == 0:
        print("Not Prime!")
        break
else:
    print("Prime!")

# Patterns
n = int(input("Enter a number: "))

for i in range(n):
    for j in range(n):
        print('*', end=' ')
    print()

# Square Patterns
n = int(input())

print('-------------------')
for i in range(n):
    for j in range(n):
        print(i+1, end=' ')
    print()
 
print('-------------------')   
for i in range(n):
    for j in range(n):
        print(j+1, end=' ')
    print()
 
print('-------------------')   
for i in range(n):
    for j in range(n):
        print(n-i, end=' ')
    print()
    
print('-------------------')   
for i in range(n):
    for j in range(n):
        print(n-j, end=' ')
    print()

# Triangle Patterns
n = int(input())

print('-------------------')
for i in range(1, n+1):
    for j in range(i):
        print(j+1, end=' ')
    print()
 
print('-------------------')   
for i in range(1, n+1):
    for j in range(i):
        print(i+j, end=' ')
    print()
 
print('-------------------')
num = 1
for i in range(1, n+1):
    for j in range(i):
        print(num, end=' ')
        num += 1
    print()

# Character Patterns
a = ord('a')
A = ord('A')
n = int(input())

print('-------------------')
for i in range(1, n+1):
    for j in range(n):
        print(chr(A+j), end=' ')
    print()
 
print('-------------------')   
for i in range(1, n+1):
    for j in range(n):
        print(chr(A+i+j-1), end=' ')
    print()

# For loops

n = int(input())

for i in range(1, n, 2):
    print(i, end=' ')


# Isosceles Pattern

n = int(input())

for i in range(1, n+1):
    for j in range(n-i):
        print(' ', end='')
    
    for j in range(i):
        print(i+j, end='')
    
    for j in range(i-1):
        print(2*(i-1)-j, end='')
        
    print()

# Diamond Pattern for Odd Number
n = int(input())

for i in range(1, 2*n, 2):
    s = abs(n-i)//2
    if i <= n:
        for j in range(s):
            print(' ', end='')
        
        for j in range(i):
            print('*', end='')
    else:
        for j in range(s):
            print(' ', end='')

        for j in range(2*n-i):
            print('*', end='')
    print()

# Functions
n, r = int(input()), int(input())

def fact(n):
    if n == 0: return 1
    return n*fact(n-1)
    
def nCr(n, r):
    return fact(n)//(fact(r)*fact(n-r))

print(nCr(n, r))
