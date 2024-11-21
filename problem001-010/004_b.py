import sys

def rotate_180(grid):
    nrows = 4
    ncols = 4
    
    for i in range(nrows//2):
        for j in range(ncols):
            grid[0+i][0+j], grid[nrows-1-i][ncols-1-j] = grid[nrows-1-i][ncols-1-j], grid[i][j]

def main():
    input_data = sys.stdin.readlines()
    grid = []
    for line in input_data:
        grid.append(line.split())
    rotate_180(grid)

    res = []
    for line in grid:
        res.append(' '.join(line))
    
    for line in res:
        print(line)
    # sys.stdout.write(f"{res}\n")

if __name__ == '__main__':
    main()