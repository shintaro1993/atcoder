import sys

def sumv(n, x, a):
    result = 0
    for i in range(n):
        if x & (1 << i):
            result += a[i]
    return result

def main():
    data = sys.stdin.read().splitlines()
    n, x = list(map(int, data[0].split()))
    a = list(map(int, data[1].split()))

    print(sumv(n, x, a))

if __name__ == '__main__':
    main()