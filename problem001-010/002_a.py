import sys

def main():
    input_data = sys.stdin.read().splitlines()
    a, b = map(int, input_data.split())
    
    print(max(a, b))

if __name__ == '__main__':
    main()