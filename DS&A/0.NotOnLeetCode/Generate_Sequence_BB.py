# Starting from 1, generate a sequence - which denotes the operations used to reach the target
# 	* multiple by 2
# 	* floor division by 3

def sequence(target,current,result):

    if current == target:
        return result
    if target%2==0:
        if current < target:
            current*=2
            result = result+"*"

        if current > target:
            current=current//3
            result = result+"/"
    else:
        if current < target:
            current*=2
            result = result+"*"

        if current > target:
            current=current//3
            result = result+"/"

    return sequence(target, current, result)



for x in [1,2,8,10,3]:
    print(sequence(x,1,""))
