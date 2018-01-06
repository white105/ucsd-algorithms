# Uses python3
import sys

def get_change(m):
    coin_count = 0
    while (m > 0):
        if (m >= 10):
            m = m - 10
            coin_count += 1
        elif (m >= 5 and m <= 10):
            m = m - 5
            coin_count += 1
        elif (m >= 1 and m <= 5):
            m = m - 1
            coin_count += 1

    return coin_count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
