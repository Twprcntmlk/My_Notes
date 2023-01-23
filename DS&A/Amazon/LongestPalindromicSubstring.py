#Time:O(2n) Space:O(1)
def longestPalindrome(s):
    if len(s) <= 1:
        return s
    start = end = 0
    length = len(s)
    result=[] # = "" just hold 1 answer
    currentMax=-1
    def get_max_len(s, left, right):
        while left >=0 and right < length and s[left] == s[right]:
            left -= 1
            right += 1
        return {"length":(right - left-1), "string":s[left+1:right]}

    for i in range(len(s)):
        max_len_1 = get_max_len(s, i, i)
        max_len_2 = get_max_len(s, i, i+1)
        if max_len_1["length"] > currentMax :
            result.append(max_len_1["string"])
        if max_len_2["length"] > currentMax :
            result.append(max_len_2["string"])
        currentMax = max(currentMax, max_len_1["length"], max_len_2["length"])
    return result[-1]


for s in ["bbbbbbbb","babad","cbbd",""]:
    print(longestPalindrome(s))
