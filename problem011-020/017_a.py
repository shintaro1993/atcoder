import sys

def check(s):
    i = 0
    n = len(s)
    while i < n:
        if i < n-1 and s[i] == 'c' and s[i+1] == 'h':
            i += 2
            continue
        if s[i] in "oku":
            i += 1
            continue
        return False
    return True

def main():
    data = sys.stdin.readline().rstrip()
    
    if check(data):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()