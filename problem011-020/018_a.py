import sys

def order(a, i, n):
    x = a[i]
    reversed_a = sorted(a, reverse=True)
    for j in range(n):
        if reversed_a[j] == x:
            return j + 1
    return None

def main():
    data = sys.stdin.readlines()
    data = list(map(int, data))
    n = len(data)
    
    for i in range(n):
        print(order(data, i, n))

if __name__ == '__main__':
    main()