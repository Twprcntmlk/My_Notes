def BananaBoat(string):
    testArr = string.lower()
    seen={}

    for idx, ele in enumerate(testArr):
        i=idx+1
        while i <= len(testArr):
            if testArr[idx:i] not in seen:
                seen[testArr[idx:i]]=1
            else:
                seen[testArr[idx:i]]+=1
            i+=1
print(BananaBoat("BananaBoat"))
