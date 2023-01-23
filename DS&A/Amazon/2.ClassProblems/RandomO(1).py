#Time: O(1)
#Space: O(N)
def __init__(self):
    self.randomSet=set()

def insert(self, val: int) -> bool:
    if val in self.randomSet:
        return False
    else:
        self.randomSet.add(val)
        return True

def remove(self, val: int) -> bool:
    if val in self.randomSet:
        self.randomSet.remove(val)
        return True
    else:
        return False

def getRandom(self) -> int:
    return (choice(list(self.randomSet)))
    #choice() is an inbuilt function that returns a random item from a list, tuple, or string
