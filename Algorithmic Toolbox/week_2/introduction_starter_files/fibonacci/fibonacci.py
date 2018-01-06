# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    else:
        arr = [0, 1]

        for i in range(2, n + 1):
            arr.append(arr[i - 1] + arr[i - 2])

        return arr[n]

n = int(input())
print(calc_fib(n))
