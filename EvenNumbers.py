def print_even_numbers(numbers):
    if not numbers:
        return
    num = numbers[0]
    if num % 2 == 0:
        print(num)
    print_even_numbers(numbers[1:])
