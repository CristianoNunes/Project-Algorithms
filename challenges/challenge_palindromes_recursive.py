def is_palindrome_recursive(word, little, big):
    if ((not word) or (word[little] != word[big])):
        return False
    elif (little > big):
        return True
    else:
        return is_palindrome_recursive(word, little + 1, big - 1)
