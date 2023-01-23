def sunset(buildings, direction):

    if direction=="EAST":
        BuildingList = list(reversed(buildings))

    if direction=="WEST":
        BuildingList = buildings

    minimum=0
    array= []
    # print(BuildingList)
    for idx,x in enumerate(BuildingList):
        # print(x,minimum, idx,array)
        if x > minimum and direction=="WEST":
            array.append(idx)
            minimum = x
        if x > minimum and direction=="EAST":
            array.insert(0,len(BuildingList)-1-idx)
            minimum = x
    return array


buildings = [3, 5, 4, 4, 3, 1, 3, 2]
direction = "WEST"
buildings1 = [3, 5, 4, 4, 3, 1, 3, 2]
direction1 = "EAST"
for x in [(buildings,direction),(buildings1,direction1)]:
    print(sunset(x[0],x[1]))
