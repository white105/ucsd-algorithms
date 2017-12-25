# Uses python3
import sys

def euclidGCD(a, b):
    if (b == 0):
        return a
    else:
        a_prime = a % b
        return euclidGCD(b, a_prime)

def lcm(a, b):
    return (a * b) // euclidGCD(a, b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
