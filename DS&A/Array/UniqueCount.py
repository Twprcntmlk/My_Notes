from collections import Counter;
import pandas as pd
def uniqueCount(arr):
    table={}
    for x in arr:
        if x not in table:
            table[x]=1
        else:
            table[x]+=1
    current = None
    for k,v in table.items():
        if v == current:
            return False
        else:
            current = v
    return True










for arr in [[1,2,2,3,3,3,4,4,4,4],[1,1,2,2,3,3],[],[1],[0,0,0,0,0]]:
    print(uniqueCount(arr))
