def fasterFibonacci(n):
    current,after = 0,1
    for i in range(n):
        current,after = after,current+after
    return current

print(fasterFibonacci(36))