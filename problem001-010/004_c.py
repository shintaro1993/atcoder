import sys

def rotate(nums, N):
    N %= 30
    for i in range(N):
        l = (i%5) + 0
        r = (i%5) + 1
        nums[l], nums[r] = nums[r], nums[l]
        

def main():
    input_data = sys.stdin.readline().rstrip()
    N = int(input_data)
    card_list = ['1', '2', '3', '4', '5', '6']

    rotate(card_list, N)
    sys.stdout.write(f"{''.join(card_list)}\n")

if __name__ == '__main__':
    main()