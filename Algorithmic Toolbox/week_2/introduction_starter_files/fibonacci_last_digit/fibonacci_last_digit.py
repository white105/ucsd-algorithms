# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if (n <= 1):
        return n
    else:
        arr = [0, 1]

        for i in range(2, n + 1):
            arr.append((arr[i - 1] + arr[i - 2]) % 10)

        return arr[n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
