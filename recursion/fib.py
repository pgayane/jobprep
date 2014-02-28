

def fib(n):
    if n == 0:
        return 0
    elif n < 3:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':

    for i in range(0, 10):
        print fib(i)
