def longestWord(words):
    ans = ""
    wordset = set(words)
    for word in words:
        if len(word) > len(ans) or len(word) == len(ans) and word < ans:
            if all(word[:k] in wordset for k in range(1, len(word))):
                ans = word

    return ans


words = ["a","banana","app","appl","ap","apply","apple"]
print(longestWord(words))
