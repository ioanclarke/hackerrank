def checkMagazine(magazine, note):
    magazine_dict = {}
    for word in magazine:
        magazine_dict[word] = magazine_dict.get(word, 0) + 1
    for word in note:
        if word in magazine_dict:
            magazine_dict[word] = magazine_dict[word] - 1
            if magazine_dict[word] == 0:
                del magazine_dict[word]
        else:
            print('No')
            return
    print('Yes')


magazine = 'two times three is not four'.split()
note = 'two times two is four'.split()
checkMagazine(magazine, note)
