def trap(height):
    waterLevel = []
    left = 0

    for h in height:
        left = max(left, h)
        waterLevel += [left] # over-fill it to left max height

    right = 0

    for i, h in reversed(list(enumerate(height))):
        right = max(right, h)
        print(waterLevel[i],right,h)
        waterLevel[i] = min(waterLevel[i], right) - h # drain to the right height

        print(waterLevel)
    return sum(waterLevel)


height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))
