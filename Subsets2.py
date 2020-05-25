def traverse(inp, finalAns, ans, index, include):
    if index == len(inp):
        finalAns.append(ans)
        return
    lst = []
    lst.extend(ans)
    if include:
        lst.append(inp[index])
    traverse(inp, finalAns, lst, index + 1, False)
    traverse(inp, finalAns, lst, index + 1, True)


def subsetsWithDup(inp):
    ans = []
    traverse(inp, ans, [], 0, False)
    traverse(inp, ans, [], 0, True)
    uniq = set()
    for lst in ans:
        st = ""
        lst = sorted(lst)
        for i in lst:
            st += str(i)
            st += ','
        uniq.add(st)
    finalAns = [[]]
    for s in uniq:
        if len(s)>0:
            lst = list(map(int, s[:-1].strip().split(",")))
            finalAns.append(lst)
    return finalAns


if __name__ == '__main__':
    print(subsetsWithDup([2,2]))
