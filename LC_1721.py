def solve(inp):
    st = []
    cnt = 0
    for c in inp:
        if c == '(':
            st.append(c)
            cnt += 1
        else:
            if len(st) > 0 and st[-1] == '(':
                st.pop()
                cnt -= 1
            else:
                st.append(c)
                cnt += 1
    return cnt


print(solve('()))(('))
