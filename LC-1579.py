def Kstart(aString):
    # write your code here
    lst = [0] * 26
    for a in aString:
        lst[ord(a) - ord('a')] += 1

    lst.sort()
    counter = []
    for i in lst:
        if i > 0:
            counter.append(i)
    n = len(counter)
    ans = 0
    for i in range(n):
        j = i
        while j > 0 and counter[j - 1] > 0 and 0 < counter[j] <= counter[j - 1]:
            v1 = counter[j - 1] - counter[j]
            ans += v1 + 1
            counter[j - 1] = counter[j - 1] - v1 - 1
            j -= 1
    return ans


if __name__ == '__main__':
    print(Kstart('aabbcccddd'))
