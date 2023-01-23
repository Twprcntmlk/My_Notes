def solve(self, sentence):
    startIdx=0
    endIdx=len(sentence)-1

    while startIdx < endIdx:
        sentence[startIdx],sentence[endIdx] = sentence[endIdx],sentence[startIdx]
        startIdx+=1
        endIdx-=1


    start=0
    for idx, char in enumerate(sentence):
        if char == " ":

            helper(start,idx-1,sentence)
            start=idx+1

        if idx == len(sentence)-1:
            helper(start,len(sentence)-1,sentence)


    return sentence

def helper(startIdx,endIdx,sentence):
        while startIdx < endIdx:
            sentence[startIdx],sentence[endIdx] = sentence[endIdx],sentence[startIdx]
            startIdx+=1
            endIdx-=1
