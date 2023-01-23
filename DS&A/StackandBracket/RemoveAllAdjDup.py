#Stack Method

def removeDuplicates(self, s: str,) -> str:
    stack = []
    for char in s:
        if not stack or stack[-1][0]!=char:
            stack.append([char,1])
        elif stack[-1][0]==char:
            stack[-1][1]+=1
        if stack[-1][1]==2:
            stack.pop()
    return "".join([x for x,y in stack])


#Recursion
def removeDuplicates(self, String: str) -> str:
    for i in range(len(String) - 1):
        if (String[i] == String[i+1]):
            String = String.replace(String[i] + String[i],'')
            return self.removeDuplicates(String)
    return String
