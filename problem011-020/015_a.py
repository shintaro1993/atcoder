import sys

def main():
    data = sys.stdin.readlines()
    data = [line.rstrip() for line in data]
    s1 = data[0]
    s2 = data[1]

    if len(s1) > len(s2):
        print(s1)
    else:
        print(s2)

if __name__ == '__main__':
    main()