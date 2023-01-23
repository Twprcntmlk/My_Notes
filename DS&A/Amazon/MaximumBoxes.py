def maximumUnits(boxTypes, truckSize):
    boxTypes.sort(key=lambda x: x[1], reverse=True )
    maxUnits=0
    filledSpace = 0
    
    for box in boxTypes:
        filledSpace+= box[0]

        if filledSpace <= truckSize:
            maxunits+=box[0]*box[1]

        else:
            remainingSpace = truckSize - (filledSpace - box[0])
            maxunits+=(remainingSpace*box[1])
            break

    return maxunits
