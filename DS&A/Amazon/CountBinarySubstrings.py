def countBinarySubstrings(self, s: str) -> int:
    ones, zeros, ans = 0, 0, 0

    for i in range(len(s)):
        if s[i] == '0':
            zeros = 1 if i > 0 and s[i - 1] != '0' else zeros + 1
            if zeros <= ones:
                ans += 1
        else:
            ones = 1 if i > 0 and s[i - 1] != '1' else ones + 1
            if ones <= zeros:
                ans += 1
    return ans
