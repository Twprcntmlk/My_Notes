# Time Complexity: O(NlogN).
# Space Complexity O(N)
def meetingRooms(meetings):
    start = sorted([x[0] for x in meetings])
    end = sorted([x[1] for x in meetings])
    res= 0
    count = 0
    startPointer= 0
    endPointer = 0
    while startPointer < len(meetings):
         # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
        if start[startPointer] < end[endPointer]:
            startPointer+=1
            count+=1
        else: # Free up a room and increment the end_pointer.
            endPointer+=1
            count-=1
        res=max(res, count) #we keep track the largest amount of open rooms there were at at time
    return res
######################################################################################
#Time Complexity: O(NlogN)
# Space Complexity O(N)
def minMeetingRooms(intervals):
    # If there is no meeting to schedule then no room needs to be allocated.
    if not intervals:
        return 0
    rooms = []# The heap initialization
    # Add the first meeting. We have to give a new room to the first meeting.
    heapq.heappush(rooms, intervals[0][1])
    # Sort the meetings in increasing order of their start time.
    intervals.sort(key= lambda x: x[0])

    for interval in intervals[1:]: # For all the remaining meeting rooms

        # If the room due to free up the earliest is free, assign that room to this meeting.
        if rooms[0] <= interval[0]:
            heapq.heappop(rooms)

        # If a new room is to be assigned, then also we add to the heap,
        # If an old room is allocated, then also we have to add to the heap with updated end time.
        heapq.heappush(rooms, interval[1])

    # The size of the heap tells us the minimum rooms required for all the meetings.
    return len(rooms)

# [0,5,10]
# [10,30,30]
# meetings=[[0,30],[5,10],[10,30]]
# meetings=[[0,30],[5,10],[1,4]]
# print(meetingRooms(meetings))
