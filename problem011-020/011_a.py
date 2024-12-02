import sys

def next_month(month):
    month += 1
    if month == 13:
        month = 1
    return month

def main():
    idata = sys.stdin.readline().rstrip()
    month = int(idata)
    print(next_month(month))

if __name__ == '__main__':
    main()