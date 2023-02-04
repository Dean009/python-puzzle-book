def filter_palindromes(strings):
    palindromes = []

    for string in strings:
        if string == string[::-1]:
            palindromes.append(string)

    return palindromes


print(filter_palindromes(["cat", "dog", "racecar", "deified", "giraffe"]))
