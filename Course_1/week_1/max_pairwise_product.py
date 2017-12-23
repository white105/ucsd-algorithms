# Uses python3
n = int(input())
arr = [int(x) for x in input().split()]
assert(len(arr) == n)

def MaxPairwiseProductFast(arr):

    n = len(arr)

    largest_index = -1
    for i in range(0, n):
        if (largest_index == -1 or arr[i] > arr[largest_index]):
            largest_index = i

    second_largest_index = -1
    for j in range(0, n):
        if ((j != largest_index) and (arr[j] > arr[second_largest_index] or second_largest_index == -1)):
            second_largest_index = j

    return (int(arr[largest_index]) * int(arr[second_largest_index]))

print(MaxPairwiseProductFast(arr))
