# namedtuple()
# factory function for creating tuple subclasses with named fields
# deque
# list-like container with fast appends and pops on either end
# ChainMap
# dict-like class for creating a single view of multiple mappings
# Counter
# dict subclass for counting hashable objects
# OrderedDict
# dict subclass that remembers the order entries were added
# defaultdict
# dict subclass that calls a factory function to supply missing values
# UserDict
# wrapper around dictionary objects for easier dict subclassing
# UserList
# wrapper around list objects for easier list subclassing
# UserString
# wrapper around string objects for easier string subclassing


from collections import Counter

#space and cases are counted differently
string="thereisnocowlevel"

print(Counter(string))
print(Counter(string).items())
print(Counter(string).keys())
print(Counter(string).values())
print(Counter(string).most_common(3))
print(Counter(string).most_common()[:-3-1:-1])
#########################
count = Counter(nums)
sorted(nums, key=lambda x: (count[x], x), reverse=True)
######################
