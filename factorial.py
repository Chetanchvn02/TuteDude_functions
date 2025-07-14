#Factorial using loop
def factorial(n):
    f=1
    for n in range(1,n+1):
        f = f * n
    return f

num = int(input("Enter the number: "))
result = factorial(num)
print("Factorial of the",num,"is",result)

#Factorial using recursion
'''
def fact(n):
    if (n == 1 or n == 0):
        return 1
    return n * fact(n-1)

num = 5
print(fact(num))
'''