def GridTraveler(x,y):
    # base cases
    if x==1 and y ==1:
        return 1
    if x==0 or y ==0:
        return 0

    return GridTraveler(x-1,y) + GridTraveler(x,y-1)

print(GridTraveler(2,2))
