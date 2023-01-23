# Time Complexity: O(N^2), where N is the length of stations.
# Space Complexity: O(N), the space used by dp.

def minRefuelStops(target, startFuel, stations):
    dp = [startFuel] + [0] * len(stations)
    for idx, (location, capacity) in enumerate(stations):
        for t in range(idx, -1, -1):
            if dp[t] >= location:
                dp[t+1] = max(dp[t+1], dp[t] + capacity)

    for idx, d in enumerate(dp):
        if d >= target:
            return idx
    return -1


####Heaps################################################################################
# Time Complexity:O(NlogN), where N is the length of stations.
# Space Complexity: O(N), the space used by pq.

def minRefuelStops(self, target, tank, stations):
    pq = []  # A maxheap is simulated using negative values
    stations.append((target, float('inf')))

    ans = prev = 0
    for location, capacity in stations:
        tank -= location - prev
        while pq and tank < 0:  # must refuel in past
            tank += -heapq.heappop(pq)
            ans += 1
        if tank < 0:
            return -1
        heapq.heappush(pq, -capacity)
        prev = location

    return ans
