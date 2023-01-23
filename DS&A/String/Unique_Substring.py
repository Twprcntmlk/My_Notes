class Solution:
    def solve(self, s):
        num = 0
        bef = ""
        for i in s:
            if i != bef:
                bef = i
                ans = 1
            else:
                ans += 1
            num += ans
        return num
