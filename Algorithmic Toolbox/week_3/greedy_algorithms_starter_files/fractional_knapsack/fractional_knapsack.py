# Uses python3
import sys

def get_optimal_value(n, capacity, weights, values):
    value = 0
    sorted_weights = []
    sorted_values = []
    frac = -99999

    for i in range(0, n):
        frac = -9999
        for j in range(0, n):
            if ((values[i] / weights[i]) > frac):
                frac = (values[i] / weights[i])




    while(capacity != 0):
        i = 0
        frac = -99999
        while(i < n):
            if ((values[i] / weights[i]) > frac):
                frac = (values[i] / weights[i])

        a = min(weights[i], capacity)
        value += (a * (values[i] / weights[i]))
        weights[i] -= a
        A[i] += a
        capacity -= a

    return value



if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(n, capacity, weights, values)
    print("{:.4f}".format(opt_value))
