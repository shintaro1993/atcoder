import sys

def calc_average_saraly(N):
    average_val = 0
    for i in range(1, N+1):
        average_val += 10000 * i
    return average_val // N

def main():
    input_data = sys.stdin.readlines()[0].rstrip()
    input_val = int(input_data)
    res = calc_average_saraly(input_val)
    sys.stdout.write(f"{res}\n")

if __name__ == '__main__':
    main()