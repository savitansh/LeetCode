def solve(s):
    st = []
    st2 = []
    for c in s:
        if c == '(':
            st.append(c)
        elif c == '*':
            st2.append(c)
        else:
            if len(st) > 0:
                st.pop()
            elif len(st2) > 0:
                st2.pop()
            else:
                return False
    return len(st) <= len(st2)


if __name__ == '__main__':
    print(solve("(())((())()()(*)(*()(())())())()()((()())((()))(*"))
