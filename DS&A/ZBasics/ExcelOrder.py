def solve(self, s):
    ans = 0
    for i in range(len(s)):
        ch = s[i]
        print(ord(ch),ord("A"))
        ans = ans * 26 + ord(ch) - ord("A") + 1
    return ans
