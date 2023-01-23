import itertools;
from collections import defaultdict;


def uniqueLetterString(s):
    def isUnique(string):
        hashtable={}
        for char in string:
            if char not in hashtable:
                hashtable[char]=1
            else:
                hashtable[char]+=1
        return [v for k,v in hashtable.items() if v == 1 ]

    table=defaultdict(lambda:0)
    count=0

    for x,y in itertools.combinations(list(range(len(s)+1)),2):
        subset = s[x:y]
        result = isUnique(subset)
        table[subset]+=len(result)


    for k,v in table.items():
        count+=v
    return count
