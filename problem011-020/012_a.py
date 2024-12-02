import sys

def main():
    data = sys.stdin.readline().rstrip()
    a, b = map(int, data.split())
    print(b, a)

if __name__ == '__main__':
    main()