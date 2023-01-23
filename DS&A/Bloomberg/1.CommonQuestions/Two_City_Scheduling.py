# Time complexity: O(n)
# Space complexity: O(n)
def twoCitySchedCost(costs):
    difference=[]
    for idx, elem in enumerate(costs):
        #need idx to get half
        difference.append([idx, elem[1]-elem[0]])

    difference.sort(key=lambda x:x[1],reverse=True)
    s=0
    for i in range(len(difference)):
        if i <len(difference)//2: #need idx to get first half / second half
            s+=costs[difference[i][0]][0]
        else:#second half
            s+=costs[difference[i][0]][1]
    return s

costs = [[10,20],[30,200],[400,50],[30,20]]
print(twoCitySchedCost(costs))

# that for multiple cities greedy solution no longer works
# it become a combinatorial optimization and I know there is an algothrim that can solve
# for this based on odd or even amount
#Benjamin Gunby at Harvard
