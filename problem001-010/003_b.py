def is_same(s, t):
    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        if s[i] == t[i]:
            continue
        elif s[i] == "@" and t[i] in "atcoder":
            continue
        elif t[i] == "@" and s[i] in "atcoder":
            continue
        elif s[i] != t[i]:
            return False
        
    return True


def main():
    s = input()
    t = input()

    if is_same(s, t):
        print("You can win")
    else:
        print("You will lose")


if __name__ == "__main__":
    main()