class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap = sticks
        heapify(heap)
        ans = 0
        while len(heap) != 1:
            first = heappop(heap)
            second = heappop(heap)
            store = first + second
            ans += store
            heappush(heap, store)
        return ans
