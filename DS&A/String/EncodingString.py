# Run-Length Encoding

# Write a function that takes in a non-empty string and returns it’s run-length encoding.

# From Wikipedia, “run-length encoding is a form of lossless data compression in which runs of data are stored as a single data value and count, rather than as the original run.” For this problem, a run of data is any sequence of consecutive, identical characters. So the run “AAA” would be run-length encoded as “3A”. The input string nca contain all sorts of special characters, including numbers.

# Sample I/Os:
# ‘AAAABBBCCD’ => ‘4A3B2C1D’
# ‘4332221111’ => ‘14233241’

# def Encoding(strr):
#     result=[]
#     startIdx = 0
#     pointer =  0
#     i=0
#     while i < len(strr):
#         print(result)
#         if strr[pointer] == strr[startIdx]:
#             pointer+=1
#         else:
#             result.append(str(pointer-startIdx))
#             result.append(strr[startIdx])

#             startIdx = pointer
#             pointer = pointer+1
#         i+=1

#     endCount = (len(strr)-(startIdx))
#     result.append(str(endCount))
#     result.append(strr[pointer-1])

#     return "".join(result)


# print(Encoding("AAAABBBCCDDDD"))

def Encoding(strr):
    i=0
    j=1
    result = []
    while i < len(strr) :
        if (j == len(strr)) or (strr[i] != strr[j]):
            result.append(str(j-i))
            result.append(strr[i])
            i=j
            j+=1
        else:
            j+=1
    return "".join(result)

print(Encoding("AAAABBBCCDDDD"))
print(Encoding("4332221111"))
