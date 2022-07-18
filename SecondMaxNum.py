def find_second_max_num(numbers):
    return find_second_max_num_recursive(numbers, numbers[0], None)


def find_second_max_num_recursive(numbers, max_num, second_max_num):
    if not numbers:
        return second_max_num
    current_num = numbers[0]
    if current_num == max_num and second_max_num is None:
        return find_second_max_num_recursive(numbers[1:], max_num, None)

    if current_num > max_num:
        second_max_num = max_num
        max_num = current_num
    elif current_num < max_num and second_max_num is None:
        second_max_num = current_num
    elif current_num > second_max_num:
        second_max_num = current_num
    return find_second_max_num_recursive(numbers[1:], max_num, second_max_num)


