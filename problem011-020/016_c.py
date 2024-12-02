import sys

def f(friends, N, M):
    for i in range(N):
        my_friends = friends[i] + [i]
        tmp = []
        for nei in friends[i]:
            tmp += friends[nei]  
        print(len(set(tmp) - set(my_friends)))

def main():
    data = sys.stdin.readlines()
    N, M  = list(map(int, data[0].split()))
    tmp = [list(map(int, line.split())) for line in data[1:M+1]]
    friends = [[] for _ in range(N)]
    
    for a, b in tmp:
        a -= 1
        b -= 1
        friends[a].append(b)
        friends[b].append(a)

    f(friends, N, M)

if __name__ == '__main__':
    main()