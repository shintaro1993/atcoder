import sys

def count_paths_between_trees(N):
    return N - 1

def main():
    input_data = sys.stdin.readline().rstrip()
    N = int(input_data)

    paths = count_paths_between_trees(N)
    print(paths)

if __name__ == '__main__':
    main()