#Time Complexity: O()
#Space Complexity: O()
class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1=nums1
        self.nums2=nums2
        self.table=defaultdict(int)

        for x in self.nums2:
            self.table[x]+=1

    def add(self, index: int, val: int) -> None:
        # remove one from table
        self.table[self.nums2[index]]-=1
        #update the array
        self.nums2[index]+=val
        #add to the table with new val
        self.table[self.nums2[index]]+=1


    def count(self, tot: int) -> int:
        count=0
        for x in self.nums1:
            diff= tot-x
            if diff in self.table:
                #we need to add by the amount because table is aggregate
                count+=self.table[diff]
        return count
