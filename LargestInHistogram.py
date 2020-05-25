def populateLastLarger(n, heights):
    st = []
    ending = []
    for i in range(n):
        ending.append(i)

    for h in range(n):
        if len(st) > 0 and heights[h] < heights[st[-1]]:
            while len(st) > 0 and heights[h] < heights[st[-1]]:
                ending[st[-1]] = h - 1
                st.pop()
        st.append(h)
    x = st[-1]
    st.pop()
    while len(st) > 0:
        ending[st[-1]] = x
        st.pop()
    return ending


def largestRectangleArea(heights):
    n = len(heights)
    nr = populateLastLarger(n, heights)
    htsrev = heights[::-1]
    nl = populateLastLarger(n, htsrev)
    nl.reverse()
    for i in range(n):
        nl[i] = n - nl[i] - 1
    maxa = 0
    for i in range(n):
        maxa = max(maxa, (heights[i] * (nr[i] - i + 1)) + (heights[i] * (i - nl[i] + 1)) - heights[i])
    return maxa

print(largestRectangleArea([2, 1, 5, 6, 2, 3]))
