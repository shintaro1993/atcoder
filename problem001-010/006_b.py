import sys

def get_n_tribonachi(N):
    if N == 1 or N == 2:
        return 0
    if N == 3:
        return 1

    prev3 = 0
    prev2 = 0
    prev1 = 1
    result = None

    for i in range(4, N+1):
        result = (prev3 + prev2 + prev1) % 10007
        prev3 = prev2
        prev2 = prev1
        prev1 = result

    return result


def main():
    input_data = sys.stdin.readline().rstrip()
    N = int(input_data)

    result = get_n_tribonachi(N)
    print(result)


if __name__ == '__main__':
    main()