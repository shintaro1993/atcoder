import sys
from collections import deque

def f(R, C, grid, sy, sx, gy, gx):
    # 開始のマスからゴールのマスへの最短距離を計算する
    q = deque()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    grid[sy][sx] = "0"
    q.append((sy, sx))

    while q:
        tmp = q.popleft()
        cr, cc = tmp[0], tmp[1]
        for i in range(4):
            nr = cr + dy[i]
            nc = cc + dx[i]

            if (nr < 0 or R <= nr) or (nc < 0 or C <= nc):
                continue
    
            if grid[nr][nc] != '.':
                continue

            q.append((nr, nc))
            tmp = int(grid[cr][cc]) + 1
            grid[nr][nc] = str(tmp)
        
    return grid[gy][gx]


def main():
    input_data = sys.stdin.read()
    array_2d = [line.split() for line in input_data.splitlines()]
    R, C = int(array_2d[0][0]), int(array_2d[0][1])
    sy, sx = int(array_2d[1][0])-1, int(array_2d[1][1])-1
    gy, gx = int(array_2d[2][0])-1, int(array_2d[2][1])-1
    grid = []
    
    for i in range(3, R+3):
        grid.append(list(array_2d[i][0]))
    
    res = f(R, C, grid, sy, sx, gy, gx)
    print(res)

if __name__ == '__main__':
    main()