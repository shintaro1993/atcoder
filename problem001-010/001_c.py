import math
from decimal import Decimal, ROUND_HALF_UP

def get_wind_direction(angle):
    directions = [
        ("S",168.75, 191.25),
        ("NNE", 11.25, 33.75),
        ("SSW", 191.25, 213.75),
        ("NE", 33.75, 56.25),
        ("SW", 213.75, 236.25),
        ("ENE", 56.25, 78.75),
        ("WSW", 236.25, 258.75),
        ("E", 78.75, 101.25),
        ("W", 258.75, 281.25),
        ("ESE", 101.25, 123.75),
        ("WNW", 281.25, 303.75),
        ("SE", 123.75, 146.25),
        ("NW", 303.75, 326.25),
        ("SSE", 146.25, 168.75),
        ("NNW", 326.25, 348.75)
    ]

    for direction, lower, upper in directions:
        lower = Decimal(lower).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        upper = Decimal(upper).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        if lower <= angle < upper:
            return direction
    return "N"


def get_wind_force(speed):
    table = [
        (0, 0.0, 0.2),
        (5, 8.0, 10.7),
        (10, 24.5, 28.4),
        (1, 0.3, 1.5),
        (6, 10.8, 13.8),
        (11, 28.5, 32.6),
        (2, 1.6, 3.3),
        (7, 13.9, 17.1),
        (3, 3.4, 5.4),
        (8, 17.2, 20.7),
        (4, 5.5, 7.9),
        (9, 20.8, 24.4)
    ]

    for force, lower, upper in table:
        lower = Decimal(lower).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        upper = Decimal(upper).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        if lower <= speed <= upper:
            return force
    return 12


def main():
    angle, distance = map(int, input().split())

    rounded_angle = Decimal(angle/Decimal('10')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    rounded_value = Decimal(Decimal(distance) / Decimal('60')).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

    wind_force = get_wind_force(rounded_value)
    wind_direction = get_wind_direction(rounded_angle)

    if wind_force == 0:
        wind_direction = "C"

    print(wind_direction, wind_force)

if __name__ == '__main__':
    main()