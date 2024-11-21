import sys
from itertools import permutations
from math import factorial

def flip(coins, ncoins):
    for i in range(ncoins):
        for j in range(i+1, ncoins):
            if coins[j][0] % coins[i][0] == 0:
                coins[j][1] *= -1

def count_front(coins, ncoins):
    n = 0
    for coin in coins:
        if coin[1] == 1:
            n += 1
    return n

def f(input_coins):
    # coin[0]: ®”
    # coin[1]: -1‚Ì‚Æ‚«— C1‚Ì‚Æ‚«•\
    nfront = 0
    ncoins = len(input_coins)
    for perm in permutations(input_coins):      
        coins = [list(coin) for coin in perm]
        flip(coins, ncoins)
        nfront += count_front(coins, ncoins)
    
    return nfront / factorial(ncoins)

def main():
    input_data = sys.stdin.read().splitlines()
    N = int(input_data[0])
    input_coins = input_data[1:]

    input_coins = [[int(elem), 1] for elem in input_coins]
    res = f(input_coins)
    print(res)
    
if __name__ == '__main__':
    main()