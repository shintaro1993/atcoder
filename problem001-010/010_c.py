import sys
from math import sqrt

def get_dist(sx, sy, tx, ty, girlx, girly):
    d1 = sqrt((sx - girlx) ** 2 + (sy - girly) ** 2)
    d2 = sqrt((tx - girlx) ** 2 + (ty - girly) ** 2)
    return d1 + d2

def can_drop(dist, T, V):
    return dist <= T * V

def is_drop_girl_house(girls, n, sx, sy, tx, ty, T, V):
    for i in range(n):
        dist = get_dist(sx, sy, tx, ty, girls[i][0], girls[i][1])
        if can_drop(dist, T, V):
            return "YES"
    return "NO"

def main():
    input_data = sys.stdin.read()
    array_2d = [line.split() for line in input_data.splitlines()]
    sx, sy, tx, ty, T, V = map(int, array_2d[0])

    n = int(array_2d[1][0])
    girls = []
    for i in range(2, 2+n):
        girls.append(list(map(int, array_2d[i])))

    print(is_drop_girl_house(girls, n, sx, sy, tx, ty, T, V))
    
    
if __name__ == '__main__':
    main()