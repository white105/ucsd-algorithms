#Uses python3

import sys
import numpy

def max_dot_product(a, b):
    #write your code here
    res = 0
    sorted_a = sorted(a)
    sorted_b = sorted(b)

    for i, j in zip(sorted_a, sorted_b):
        res += i * j

    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
