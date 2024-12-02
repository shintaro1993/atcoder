import sys

def get_max_num(n, A, ncolor):
    counter = [0] * ncolor
    for a, b in A:
        counter[a] += 1
        if b+1 < ncolor:
            counter[b+1] -= 1
    for i in range(1, ncolor):
        counter[i] += counter[i-1]
    return max(counter)

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    A = [list(map(int, line.split())) for line in data[1:n+1]]
    maxv = 0
    for _, b in A:
        maxv = max(maxv, b)

    print(get_max_num(n, A, maxv+1))

if __name__ == '__main__':
    main()