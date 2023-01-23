class Solution:
    def solve(self, s):
        count=0
        table={
            "(":")"
        }

        stack=[]
        for char in s:
            if char in table.keys():
                stack.append(char)

            else:
                if not stack and char == ")":
                    count+=1
                elif stack and char == ")":
                    stack.pop()
                else:
                    count+=1
        return count + len(stack)
