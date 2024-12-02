import sys

def check(A, B, C):
    if A + B == C and A - B == C:
        return "?"
    if A + B == C:
        return "+"
    if A - B == C:
        return "-"
    if A + B != C or A - B != C:
        return "!"

def main():
    stream = sys.stdin.readline().split()
    A, B, C = list(map(int, stream))

    print(check(A, B, C))

if __name__ == '__main__':
    main()