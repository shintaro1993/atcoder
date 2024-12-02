from typing import List

REPLACEMENT_CHARS = set("atcoder")

def isreplace(s: str, t: str) -> bool:
    return (s == "@" and t in REPLACEMENT_CHARS) or (t == "@" and s in REPLACEMENT_CHARS)

def can_win(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    for sc, tc in zip(s, t):
        if sc == tc:
            continue
        if isreplace(sc, tc):
            continue
        return False
    
    return True

def main():
    s = input()
    t = input()

    if can_win(s, t):
        print("You can win")
    else:
        print("You will lose")

if __name__ == "__main__":
    main()