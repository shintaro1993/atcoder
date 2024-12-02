import sys

def check(N, K, questions, level=0, val=0):
    if level >= N:
        return val == 0

    for i in range(K):
        if check(N, K, questions, level + 1, val ^ questions[level][i]):
            return True

    return False

def main():
    stream = sys.stdin.readlines()
    N, K = list(map(int, stream[0].split()))
    questions = [list(map(int, line.split())) for line in stream[1:N+1]]

    if check(N, K, questions):
        print("Found")
    else:
        print("Nothing")

if __name__ == '__main__':
    main()