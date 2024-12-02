import sys

def min_npress(a, b):
    tmp1 = abs(b - a)
    tmp2 = abs(10 - tmp1)
    return min(tmp1, tmp2)

def main():
    data = sys.stdin.read().splitlines()
    a = int(data[0])
    b = int(data[1])

    print(min_npress(a, b))

if __name__ == '__main__':
    main()