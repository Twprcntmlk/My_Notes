def toObject(string):
    table={}
    Array=string.split("/n") #O(n+m+k)

    for x in Array:
        equals=x.index('=')

        key=x[0:equals]
        value=x[(equals+1):len(x)]
        table[key]=value
    return table



string="thereisnocowlevel=wirtsleg/nHowtoMainaDragon=Sword=Slashing=Monkeys"

print(toObject(string))
