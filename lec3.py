def factorial(n, sum = 1):
    while n!= 1:
        sum *= n
        n -= 1
    return(sum)
print(factorial(int(input("> "))))1