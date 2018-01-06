# Uses python3
import sys

def get_majority_element(a, left, right):
    if (left == right):
        return -1
    if (left + 1 == right):
        return a[left]

    left_element = get_majority_element(a, left, (left + right - 1) // 2 + 1)
    right_element = get_majority_element(a, (left + right - 1) // 2 + 1, right)

    left_counter = 0
    for i in range(left, right):
        if (a[i] == left_element):
            left_counter += 1
    if (left_counter > (right - left) // 2):
        return left_element

    right_counter = 0
    for i in range(left, right):
        if (a[i] == right_element):
            right_counter += 1
    if (right_counter > (right - left) // 2):
        return right_element

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
