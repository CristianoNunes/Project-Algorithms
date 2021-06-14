def is_anagram(first_string, second_string):
    str1 = ''.join(sorted(first_string))
    str2 = ''.join(sorted(second_string))

    return str1 == str2
