import sys

def get_max_value(X, Y):
    """ 
    >>> get_max_value(2, 1)
    2
    >>> get_max_value(1, 2)
    2
    >>> get_max_value(10, 1)
    10
    """

    return max(X, Y)

def main():
    input_data = sys.stdin.readlines()[0].split(" ")
    input_val1 = int(input_data[0])
    input_val2 = int(input_data[1])
    res = get_max_value(input_val1, input_val2)
    sys.stdout.write(f"{res}\n")

if __name__ == '__main__':
    main()
    # import doctest
    # doctest.testmod()