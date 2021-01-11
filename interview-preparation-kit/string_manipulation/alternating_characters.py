

def alternatingCharacters(s):
    print(s)
    deletions = 0
    while True:
        cur = None
        changed = False
        for i, char in enumerate(s):
            if char == cur:
                s = s[:i] + s[i+1:]
                print(s)
                deletions += 1
                changed = True
                break
            cur = char
        if changed == False:
            break
    return deletions


fin = open('input.txt')
s = fin.read().split('\n')
print(len(s))
s = 'AAABBB'
print(alternatingCharacters(s))
