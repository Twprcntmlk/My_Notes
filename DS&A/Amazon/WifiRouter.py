def wifiRouters(buildingCount, routerLocation, routerRange):
    n = len(buildingCount)
    routerCount = [0]*n

    for i in range(len(routerLocation)):
        coveringRange = routerRange[i]
        startIdx = max(0, routerLocation[i]-1-coveringRange)
        endIdx = min(n-1, routerLocation[i]-1+coveringRange)

        routerCount[startIdx] += 1
        if endIdx < n-1:
            routerCount[endIdx+1] -= 1
        print(routerCount)
    for i in range(1, n):
        routerCount[i] += routerCount[i-1]

    count = 0
    for i in range(n):
        if routerCount[i] >= buildingCount[i]:
            count += 1
    return count
