def length_of_list(list):
    interim_len = 0
    if list:
        list.pop()
        interim_len = 1 + length_of_list(list)
    return interim_len
