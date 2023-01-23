def countAndSayITERATIVE(n):
    string = '1'
    for _ in range(1,n):
        new_string = ''
        prev_char = ''
        count = 0
        for char in string:
            if char == prev_char:
                count += 1
            else:
                if count > 0:
                    new_string += str(count) + prev_char
                prev_char = char
                count = 1
        #handle last iteration
        new_string += str(count) + prev_char
        string = new_string
    return string


#RECURSIVE
def lookandsay(n):

    if n==1:
        return "1"
    prev=lookandsay(n-1)
    res=""
    count=1

    for i in range(len(prev)):
        if i == len(prev)-1 or prev[i] !=prev[i+1]:
            res+=str(count)+prev[i]

            count=1
        else:
            count+=1

    return res
