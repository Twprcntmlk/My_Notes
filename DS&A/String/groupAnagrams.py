def groupAnagrams(strs):
    result = []
    # OriginalArray = strs
    sortedArray = ["".join(sorted(x)) for x in strs]
    
    unique = set(sortedArray)
    for x in unique:
        anagramset = []
        for idx, y in enumerate(sortedArray):
            if x == y:
                anagramset.append(strs[idx])
        result.append(anagramset)
    return result

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
#######################################################################################################
