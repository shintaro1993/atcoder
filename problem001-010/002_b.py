import sys

def delete_all_vowl(string):
    result = ""
    for c in string:
        if c not in "aiueo":
            result += c
    return result

def main():
    input_data = sys.stdin.readlines()[0].rstrip()
    word = input_data
    res = delete_all_vowl(word)
    sys.stdout.write(f"{res}\n")

if __name__ == '__main__':
    main()