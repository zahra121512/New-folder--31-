def factorial(n):
    '''this is a recursive functipoon to find the factorial of a given number'''
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("enter a number: "))

if num < 0:
    print("factorial does not exist for negetive numbers")
else:
    print(factorial.__doc__)
    print(f"the factorial of {num} is {factorial(num)}")