def findAllConcatenatedWordsInADict(words):

    word_sets = set(words)
    res = []

    # use dp to solve each word
    for word in words:
        if word == '':
            continue
        word_sets.remove(word)


        dp = [0] * (len(word) + 1)
        dp[0] = 1

        for i in range(1, len(word) + 1):
            for j in range(i):
                if dp[j] == 1 and word[j:i] in word_sets:
                    dp[i] = 1
        if dp[-1] == 1:
            res.append(word)
        word_sets.add(word)
####################################################################################################

def DFSfindAllConcatenatedWordsInADict(words) :
    wordset = set(words)
    res = set()

    def dfs(word):
        result = 1
        for i in range(1, len(word)):
            print(word[:i])
            if word[:i] in wordset:
                #
                print(result, word[:i])
                result = max(result, 1 + dfs(word[i:]))

        if result == 1 and word not in wordset:
            return 0
        else:
            return result


    for word in words:
        if word not in res and dfs(word) > 1:
            print(word)
            res.add(word)

    return list(res)


# Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# print(findAllConcatenatedWordsInADict(words))


print(DFSfindAllConcatenatedWordsInADict(words))
