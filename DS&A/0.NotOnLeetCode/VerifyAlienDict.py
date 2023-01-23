# Time Complexity : O(N). Total number of characters
# Space Complexity : O(1). The only extra data structure we use is the hashmap/array for the 26 letters O(26)

def isAlienSorted(words, order):
    order_map = {}
    for index, val in enumerate(order):
        order_map[val] = index

    for word in range(len(words) - 1):

        for letter in range(len(words[word])):
            # If we do not find a mismatch letter between words[i] and words[i + 1],
            # we need to examine the case when words are like ("apple", "app").
            print(letter,len(words[word + 1]))
            if letter >= len(words[word + 1]):
                return False

            if words[word][letter] != words[word + 1][letter]:
                if order_map[words[word][letter]] > order_map[words[word + 1][letter]]:
                    return False
                # if we find the first different character and they are sorted,
                # then there's no need to check remaining letters
                break

    return True

words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(isAlienSorted(words, order))
