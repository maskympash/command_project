def fact_rec(number: int):
    if number < 0:
        return None

    if number > 0:
        return number * fact_rec(number - 1)

    else:
        return 1


def is_power_of_five(number):
    import math
    return (number > 0) and (math.log(number, 5) % 1 == 0)


def is_power_of_five(number):
    return (number > 0) and (math.log(number, 5) % 1 == 0)


def is_prime(number: int):
    from math import ceil

    number = abs(number)

    if number == 0 or number == 1:
        return False

    elif number == 2:
        return True

    end = ceil(number ** 0.5) + 1

    for i in range(2, end):
        if number % 2 == 0:
            return False

    return True


def nsd(a, b):
    if a < b:
        a,b = b,a
    while b > 0:
        a, b = b, a % b

    return a
