def fact_rec(number: int):
    if number < 0:
        return None

    if number > 0:
        return number * fact_rec(number - 1)

    else:
        return 1

print(fact_rec())
