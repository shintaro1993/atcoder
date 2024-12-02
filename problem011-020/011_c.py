import sys

def check(N, NG1, NG2, NG3):
    nglist = [NG1, NG2, NG3]
    if N in nglist:
        return False
    
    for _ in range(100):
        if N - 3 not in nglist:
            N -= 3
            continue
        if N - 2 not in nglist:
            N -= 2
            continue
        if N - 1 not in nglist:
            N -= 1
            continue
        return False

    return N <= 0

def main():
    data = sys.stdin.read().splitlines()
    N = int(data[0])
    NG1 = int(data[1])
    NG2 = int(data[2])
    NG3 = int(data[3])

    if check(N, NG1, NG2, NG3):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()