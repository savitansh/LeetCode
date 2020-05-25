def getKey(element):
    return element[0]


def merge(intervals):
    intervals.sort(key=getKey)
    st = intervals[0][0]
    en = intervals[0][1]
    n = len(intervals)
    ans = []
    for i in range(1, n):
        if intervals[i][0] >= en:
            pair = [st, en]
            ans.append(pair)
            st = intervals[i][0]
            en = intervals[i][1]
        else:
            en = max(en, intervals[i][1])
    ans.append([st, en])
    return ans


if __name__ == '__main__':
    print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
