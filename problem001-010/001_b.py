import sys

def convert_dist_to_vv(m):
    """
    
    >>> convert_dist_to_vv(100)
    '01'
    >>> convert_dist_to_vv(1000)
    '10'
    >>> convert_dist_to_vv(5000)
    '50'
    >>> convert_dist_to_vv(6000)
    '56'
    >>> convert_dist_to_vv(30000)
    '80'
    >>> convert_dist_to_vv(35000)
    '81'
    >>> convert_dist_to_vv(36000)
    '81'
    >>> convert_dist_to_vv(70000)
    '88'
    >>> convert_dist_to_vv(71000)
    '89'
    """

    m /= 1000
    if m < 0.1:
        return "00"
    elif 0.1 <= m <= 5.0:
        return f"{int(m*10):02}"
    elif 6.0 <= m <= 30.0:
        return str(int(m) + 50)
    elif 35.0 <= m <= 70.0:
        return str(int((m-30)/5 + 80))
    elif 70.0 < m:
        return "89"

def main():
    input_data = sys.stdin.read().splitlines()
    m = int(input_data[0])
    res = convert_dist_to_vv(m)
    sys.stdout.write(f"{res}\n")

if __name__ == '__main__':
    main()
    # import doctest
    # doctest.testmod()