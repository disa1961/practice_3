def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    count = {}
    for c in s1:
        count[c] = count.get(c, 0) + 1
    for c in s2:
        if c not in count or count[c] == 0:
            return False
        count[c] -= 1
    return True
