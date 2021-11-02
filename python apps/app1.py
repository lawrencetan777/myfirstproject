print("Welcome to my first app")
print("fibbonaci calculator")

data={}
data[0] = 0
data[1] = 1

def fibonacci(i):
    if i<0:
        print("This won't work")
    if i-1 not in data:
        data[i-1] = fibonacci(i-1)
    if i-2 not in data:
        data[i-2] = fibonacci(i-2)
    return data[i-1] + data[i-2]

print( " fib(100)=" + str(fibonacci(20)))