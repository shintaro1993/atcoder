import sys

def f(s, l, r):
    pref, mid, suff = s[:l], s[l:r+1], s[r+1:]
    return pref + mid[::-1] + suff

def main():
    data = sys.stdin.read().splitlines()
    s = data[0]
    N = int(data[1])
    
    for i in range(N):
        l, r = list(map(int, data[2+i].split()))
        l -= 1
        r -= 1
        s = f(s, l, r)

    print(s)

if __name__ == '__main__':
    main()