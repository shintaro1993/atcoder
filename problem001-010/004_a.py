import sys

def main():
    input_data = sys.stdin.readline()
    res = 2 * int(input_data)
    sys.stdout.write(f"{res}\n")

if __name__ == '__main__':
    main()