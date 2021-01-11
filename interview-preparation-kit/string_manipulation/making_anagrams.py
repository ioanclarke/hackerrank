def makeAnagram(a, b):
    a_dict = {}
    b_dict = {}
    for char in a:
        a_dict[char] = a_dict.get(char, 0) + 1
    for char in b:
        b_dict[char] = b_dict.get(char, 0) + 1

    deletions = 0
    for char, freq in a_dict.items():
        if char in b_dict:
            if freq > b_dict[char]:
                diff = freq - b_dict[char]
                deletions += diff
                a_dict[char] = a_dict[char] - diff
        else:
            diff = freq
            deletions += freq
            a_dict[char] = 0

    for char, freq in b_dict.items():
        if char in a_dict:
            if freq > a_dict[char]:
                diff = freq - a_dict[char]
                deletions += diff
                b_dict[char] = b_dict[char] - diff
        else:
            diff = freq
            deletions += diff
            b_dict[char] = 0

    return deletions


a = 'cde'
b = 'abc'
print(makeAnagram(a, b))
