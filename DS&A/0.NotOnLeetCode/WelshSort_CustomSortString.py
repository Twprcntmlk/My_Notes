# Space Complexity: O(1) making 1 array and 1 object and length is constant
# Time Complexity: O(n log n) sort + iterate through to convert

alphabets = ['a', 'b', 'c', 'ch', 'dd', 'd', 'e', 'f', 'ff', 'g', 'ng', 'h', 'i', 'j', 'l', 'll', 'm', 'n', 'o', 'p', 'ph', 'r', 'rh', 's', 't', 'th', 'u', 'w', 'y']

def WelshSort(words):

    alphabet_index_map = {char: idx for idx, char in enumerate(alphabets)}

    # convert words to array of indices
    word_arrays = []
    for word in words:
        word_arr = []
        idx = 0
        while idx < len(word):
            if word[idx:idx+2] in alphabet_index_map:
                word_arr.append(alphabet_index_map[word[idx:idx+2]])
                idx += 2
            else:
                word_arr.append(alphabet_index_map[word[idx:idx+1]])
                idx += 1
        word_arrays.append(word_arr)

    # sort
    word_arrays.sort()

    # convert the sorted numbers back to words
    sorted_words = []
    for word_arr in word_arrays:
        for idx, pos in enumerate(word_arr):
            word_arr[idx] = alphabets[pos]
        sorted_words.append(''.join(word_arr))

    return sorted_words

print(WelshSort(['abcd', 'abcdd']))
# ['abcdd', 'abcd']
print(WelshSort(['abcd', 'abcdd', 'abcch']))
# ['abcch', 'abcdd', 'abcd']
print(WelshSort(["d", "ddr", "nah", "dd", "dea", "ngah"]))
# ['dd', 'ddr', 'd', 'dea', 'ngah', 'nah']

# Follow up:

# How do you test the code ?
# What if now you have also capital letters ? ex. "Ddaf" use toLowerCase()
