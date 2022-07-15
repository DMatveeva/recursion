def power(n, m):
    result = 1
    if m > 0:
        result = n * power(n, m - 1)
    return result