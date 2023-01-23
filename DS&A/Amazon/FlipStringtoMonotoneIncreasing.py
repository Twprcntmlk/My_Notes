#Time O(N) Space:O(1)
def minFlipsMonoIncr(s):
    countOf1 = 0
    flips = 0
    for x in range(len(s)):
        if s[x] =="1":
            countOf1+=1
        else:
            flips+=1

        flips = min(countOf1, flips)
        print(countOf1, flips)
    return flips
    # We just want to count the extremes
    # how many 1 are on the left because we can change them 0s
    # how many 0  are on the right because we can change them 1s
    # the in betweens will be the same
    # get the min

for inputs in ["0101100011","00110","010110","00011000","0011000010","111011100100100"]: #
    print(minFlipsMonoIncr(inputs))
