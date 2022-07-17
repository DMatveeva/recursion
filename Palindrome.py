def is_palindrome(string):
    is_substring_palindrome = True
    if len(string) > 1:
        is_substring_palindrome = (string[0] == string[-1]) and is_palindrome(string[1:-1])
    return is_substring_palindrome


