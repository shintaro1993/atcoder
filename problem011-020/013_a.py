import sys

def main():
    data = sys.stdin.readline().rstrip()
    print(ord(data) - ord('A') + 1)

if __name__ == '__main__':
    main()