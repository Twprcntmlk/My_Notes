def solve(self, s1, s2):
    pointerS1=0
    pointerS2=0

    while pointerS1 <len(s1) and pointerS2 <len(s2) :
        if s1[pointerS1] == s2[pointerS2]:
            pointerS1+=1
        pointerS2+=1

    return pointerS1 == len(s1)
