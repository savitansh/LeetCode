class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglyNos = [1]
        p2 = 0
        p3 = 0
        p5 = 0
        while len(uglyNos)<1692:
            v2 = uglyNos[p2] * 2
            v3 = uglyNos[p3] * 3
            v5 = uglyNos[p5] * 5
            if (v2 <= v3 and v2 <= v5):
                if uglyNos[-1] != v2:
                    uglyNos.append(v2)
                p2 += 1
            elif (v3 <= v2 and v3 <= v5):
                if uglyNos[-1] != v3:
                    uglyNos.append(v3)
                p3 += 1
            else:
                if uglyNos[-1] != v5:
                    uglyNos.append(v5)
                p5 += 1
        return uglyNos[n-1]


if __name__ == "__main__":
    s = Solution()
    print(s.nthUglyNumber(1690))
