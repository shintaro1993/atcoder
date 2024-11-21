import sys

def main():
    input_data = sys.stdin.read().splitlines()
    N = int(input_data[0])
    res = 101
    for i in range(N):
        res = min(res, int(input_data[1+i]))
    print(res)


if __name__ == '__main__':
    main()