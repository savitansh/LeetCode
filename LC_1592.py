def findAndReplacePattern(words, pattern):
    ans = []
    for w in words:
        d = {}
        s = set()
        match = True
        if len(w) == len(pattern):
            n = len(w)
            for i in range(n):
                if pattern[i] in d:
                    x = d[pattern[i]]
                    if w[i] != x:
                        match = False
                else:
                    if w[i] in s:
                        match = False
                    else:
                        d[pattern[i]] = w[i]
                s.add(w[i])
        else:
            match = False
        if match:
            ans.append(w)
    return ans


print(findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"))
