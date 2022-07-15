def power(n, m):
    interim_power = 1
    if m > 0:
        interim_power = n * power(n, m - 1)
    return interim_power
