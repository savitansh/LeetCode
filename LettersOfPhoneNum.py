from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {'1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
                  '9': 'wxyz'}
        ans = []
        self.traverse(digits, 0, keypad, ans, '')
        return ans

    def traverse(self, digits, pos, keypad, ans, s):
        if pos >= len(digits):
            ans.append(s)
            return
        keys = keypad[digits[pos]]
        if keys == '':
            self.traverse(digits, pos + 1, keypad, ans, s)
        else:
            for key in keys:
                s2 = s + key
                self.traverse(digits, pos + 1, keypad, ans, s2)


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('212'))
