 # Time: O(n)
# Space: O(n)
def decodeString(str):
    stack  = []
    for char in s:
        if char != ']':
            stack.append(char)
        else:
            string = ""
            num = ""
            temp = ""

            while stack[-1] != '[':
                string = stack.pop() + string
            stack.pop()

            while stack and stack[-1].isdigit():
                num = stack.pop() + num

            for i in range(int(num)):
                temp += string
            stack.append(temp)
    return "".join(stack)
############################################################################
def decodeStringRecursive(s):
    def recursion(s, pos):
        result = ""
        i =  pos
        num = 0

        while i < len(s):
            char = s[i]
            if char.isdigit():
                num = num * 10 + int(char) #first 0+NUM
            elif char == '[':
                string, end = recursion(s, i + 1)
                result += num * string
                i = end
                num = 0
            elif char == ']':
                return result, i
            else:
                result += char
            i += 1

        return result, i
    return recursion(s, 0)[0]
#####################################################################################
# s = "3[a]2[bc]"
# print(decodeString(s))
