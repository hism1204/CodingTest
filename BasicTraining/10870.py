l = list(map(int, input().split()))
n = l[0]


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 20:
        return
    else:
        val = fibonacci(n - 1) + fibonacci(n - 2)
        return val


print(fibonacci(n))
