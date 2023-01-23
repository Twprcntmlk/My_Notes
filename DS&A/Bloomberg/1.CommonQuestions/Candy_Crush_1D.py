# Time Complexity: O(N*M)
# Space Complexity O(N)
def CandyCrushRecursive(string):
  result=""
  i = 0
  while i < len(string):
      temp = string[i] #handles first new char
      while 0 <= i < len(string)-1 and string[i] == string[i+1]:
          temp+=string[i+1]
          i += 1
      i += 1
      if len(temp) >= 3:
          continue
      else:
        result+=temp
  return result

  if len(result) == len(string):#if nothing has changed result
    return result
  return CandyCrushRecursive(result)   #recurse with new sting

#######################################################################################################################
# Time Complexity: O(N)
# Space Complexity O(N)
def CandyCrushStack(string):
    stack = []
    for c in string :
        if not stack or c != stack[-1][-1]:
          stack.append(c)
        elif c == stack[-1][-1]:
          stack[-1] += c
        if len(stack[-1]) >= 3:
          stack.pop()
    return ''.join(stack)

# listOfStr = [ "aaabbbccadb","aaabbbacd","aaabbbc", "aaaaaa", "aaa", "abcd", "baaabbbabbccccd"]
# for idx, el in enumerate(listOfStr):
#   print(f"{idx}: {CandyCrushRecursive(el)}")

# for idx, el in enumerate(listOfStr):
#   print(f"{idx}: {CandyCrushStack(el)}")
