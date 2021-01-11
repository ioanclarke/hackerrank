def superReducedString(s):
    while True:
        change = False
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                s = s[:i] + s[i+2:]
                change = True
                break
        if change == False:
            break
    if s == '':
        s = 'Empty String'
    return s

print(superReducedString('aaabccddd'))
