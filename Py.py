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

# Binary search
def find(search_list, value):
    binary_search_result = binary_search(search_list, value, 0, len(search_list)-1)
    print(f"===> Binary_search_result: {binary_search_result}")
    return binary_search_result

def binary_search(search_list, value, left, right):
    
    print(f"left: {left}")
    print(f"right: {right}")
    print(f"search_list[{left}:{right}]: {search_list[left:right]}")
    
    if left > right:
        print("returning -1")
        return -1
        # raise ValueError("value not in array")

    mid = (left+right)//2

    print(f"mid: {mid}")
    print(f"value == search_list[mid] => {value == search_list[mid]}")
    
    if value == search_list[mid]:
        print(f"returning mid={mid}")
        return mid
    elif value < search_list[mid]:
        return binary_search(search_list, value, left, mid-1)
    else:
        return binary_search(search_list, value, mid+1, right)

print(find([1, 3, 4, 6, 8, 9, 11], 91))

# Selection Sort

def selection_sort(arr, n):
    for i in range(n):
        curr_min = i
        for j in range(i, n):
            if arr[j] < arr[curr_min]:
                curr_min = j
        arr[i], arr[curr_min] = arr[curr_min], arr[i]
        
        
arr = [4, 6, 1, 3, 2]
selection_sort(arr, len(arr))
print(arr)
            
