# Time complexity: O(n)
# Space complexity: O(1)

def numberOfWeeks(milestones):
    maximum = max(milestones)
    total = sum(milestones) - maximum
    if total >= maximum:
        return total+maximum
    else:
        return 2*total+1

# If sum of remaining numbers is greater than or equal to the maximum milestone
# then maximum milestone can be completed along with other milestones.
# Otherwise, maximum milestone cannot be reached as it will go till the sum of remaining milestones.

# milestones = [17,2,1]
# print(numberOfWeeks(milestones))
