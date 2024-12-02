import sys
from math import ceil

def f(N, A):
    result = 0
    count = 0
    for elem in A:
        if elem != 0:
            count += 1
        result += elem
    return ceil(result/count)

def main():
    data = sys.stdin.readlines()
    data = [list(map(int, line.split())) for line in data]
    N = data[0]
    A = data[1]
    
    print(f(N, A))

if __name__ == '__main__':
    main()