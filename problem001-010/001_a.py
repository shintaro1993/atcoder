import sys

def get_hourly_snow_depth_diff(H1, H2):
    return H1 - H2

def main():
    input_data = sys.stdin.read().splitlines()
    H1 = int(input_data[0])
    H2 = int(input_data[1])
    print(get_hourly_snow_depth_diff(H1, H2))

if __name__ == '__main__':
    main()