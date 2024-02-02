def fact_rec(number: int):
    if number < 0:
        return None

    if number > 0:
        return number * fact_rec(number - 1)

    else:
        return 1

def nsd(a, b):
    if a < b:
        a,b = b,a
    while b > 0:
        a, b = b, a % b

    return a

a, b = [int(d) for d in input().split()]
print(nsd(a,b))
