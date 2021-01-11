from math import factorial

def sherlockAndAnagrams(s):
    substrings = {}
    leng = len(s)
    for i in range(leng):
        for j in range(i+1, leng+1):
            new_sub = s[i:j]
            sorted_sub = ''.join(sorted(new_sub))
            substrings[sorted_sub] = substrings.get(sorted_sub, 0) + 1
    pairs = 0
    for v in substrings.values():
        if v > 1:
            pairs += int(factorial(v)/(2*factorial(v-2)))
    return pairs


print(sherlockAndAnagrams('kkkk'))
"""
1 -> 0
2 -> 1
3 -> 3
4 -> 6
5 ->
"""
