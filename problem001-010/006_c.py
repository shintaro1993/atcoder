import sys

def find_adult_old_baby_num(N, M):
    res = ["-1", "-1", "-1"]
    for c in range(5*10**5+1):
        a = (3*N) - M + c
        b = (-2*N) + M + (-2*c)
        if a >= 0 and b >= 0:
            res[0] = str(a)
            res[1] = str(b)
            res[2] = str(c)
            break
    return res

def main():
    input_data = sys.stdin.readline().split()
    N = int(input_data[0])
    M = int(input_data[1])

    res = find_adult_old_baby_num(N, M)
    print(" ".join(res))

if __name__ == '__main__':
    main()