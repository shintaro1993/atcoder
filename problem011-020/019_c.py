import sys
import random

def isexist(s, elem):
    if elem % 2 != 0:
        return False

    while elem > 0:
        if elem // 2 in s:
            return True
        elem = elem // 2
    return False

def myfunc(a):
    count = 0
    s = set(a)
    for elem in s:
        if not isexist(s, elem):
            count += 1
    return count

def lillian(arr):
    arr_set = set(arr)
    for elem in arr:
        divisible = []
        while elem % 2 == 0:
            elem //= 2
            divisible.append(elem)

        arr_set.difference_update(set(divisible))

    return len(arr_set)

def main():
    data = sys.stdin.readlines()
    a = list(map(int, data[1].split()))
    print(myfunc(a))

    # n = 5
    # while True:
    #     random_list = [random.randint(1, 100) for _ in range(n)]
    #     r1 = myfunc(random_list)
    #     r2 = lillian(random_list)
    #     if r1 != r2:
    #         print(random_list)
    #         print(f"my result: {r1}")
    #         print(f"lillian result: {r2}")
    #         break


if __name__ == '__main__':
    main()