def LexicographicalMaxString(str):
    mx = ""
    for i in range(len(str)):
        print (i, mx)
        mx = max(mx, str[i:])
    return mx


str = "leetcode"
print(LexicographicalMaxString(str))
