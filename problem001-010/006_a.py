import sys

def main():
    input_data = sys.stdin.readline().rstrip()
    N = int(input_data[0])

    if "3" in str(N) or N % 3 == 0:
        print("YES")
    else:
        print("NO")
    

if __name__ == '__main__':
    main()