# Time complexity  O(nlogn)
# Space complexity: at worst O(n)
def merge(intervals):
    intervals.sort(key=lambda x:x[0])
    result=[intervals[0]]
    # count=1
    # total=0
    for idx in range(1,len(intervals)):
        if intervals[idx][0]<=result[-1][1]:
            result[-1][1]=max(result[-1][1],intervals[idx][1])
            # count+=1
            # total=max(count, total)
        else:
            result.append(intervals[idx])
            # count=0
    return result # total

# interval = [[1,3],[2,6],[8,10],[15,18]]
# print(merge(interval))
