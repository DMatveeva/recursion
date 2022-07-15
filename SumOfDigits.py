def sum_of_digits(num):
    interim_sum = 0
    if num > 0:
        current_digit = num % 10
        interim_sum = current_digit + sum_of_digits(num // 10)
    return interim_sum
