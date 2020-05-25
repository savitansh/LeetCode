def multiplydigit(s1, digit, shift):
    if digit == '0':
        return [0]
    res = []
    n = len(s1)
    carry = 0
    for i in range(n):
        c = int(digit) * int(s1[i])
        val = c % 10
        res.append(carry + val)
        carry = int(c / 10)
    if carry > 0:
        res.append(carry)
    if shift > 0:
        res = ([0] * shift) + res
    return res


def addResToAns(ans, res):
    carry = 0
    i = 0
    for digit in res:
        if i < len(ans):
            val = digit + ans[i] + carry
            ans[i] = val % 10
        else:
            val = digit + carry
            ans.append(val % 10)
        carry = int(val / 10)
        i += 1
    if carry > 0:
        ans.append(carry)


def mul(s1, s2):
    s1 = s1[::-1]
    s2 = s2[::-1]
    ans = []
    m = len(s2)
    for j in range(m):
        res = multiplydigit(s1, s2[j], j)
        addResToAns(ans, res)
    result = ""
    n = len(ans)
    for i in range(n):
        result += str(ans[i])
    return result[::-1]



if __name__ == '__main__':
    print(mul("99", "9"))
