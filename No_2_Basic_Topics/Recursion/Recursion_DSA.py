# || Factorial of numbers using Function & Recurtion ||
try:
    user = int(input("Enter a number:-"))
except Exception as e:
    print(e)
def recusive_factorial(n):
    if n == 1 or n == 0:
        return 1  # Base Condition
    return n * recusive_factorial(n - 1) # Recursive Relation
print(recusive_factorial(user))

# || Sum of n natural numbers using Function & Recursion ||
try:
    user = int(input("Enter a number:-"))
except Exception as e:
    print(e)
def recursive_sum(n):
    if n == 1:
        return 1  # Base Condition
    elif n == 0:
        return 0  # Base Condition
    return n + recursive_sum(n-1) # Recursive Relation
print(f"The sum of first {user} natural number is:-", recursive_sum( user))

# || A Recursive Function To count Number ||]
try:
    user_num = int(input("Enter a number:"))
except Exception as e:
    print("Please Enter Number not Word!")
def counting(n):
    if n == 0 or n == 1:
        return 1  # Base Condition
    print(n)  # Processing
    counting(n-1) # Recursive Relation
print(counting(user_num))

# || Finding Fibonacci Number Using Recursion ||
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)
for i in range(1, 11):
    print(fibonacci(i))

