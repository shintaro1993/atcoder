import sys

def calc(N, K, R):
    R.sort()
    rate = 0
    for i in range(K):
        elem = R[N-K+i]
        rate = (rate+elem) / 2
    return rate

def main():
    input_data = sys.stdin.read().splitlines()
    N, K = map(int, input_data[0].split())
    R = list(map(int, input_data[1].split()))
    res = calc(N, K, R)
    sys.stdout.write(f"{res}\n")

if __name__ == '__main__':
    main()