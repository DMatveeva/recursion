def print_elements_with_even_indices(values, index=None):
    if index is None:
        index = 0
    if not values:
        return
    if index % 2 == 0:
        print(values[0])
    index += 1
    print_elements_with_even_indices(values[1:], index)
