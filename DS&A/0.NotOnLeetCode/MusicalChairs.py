# O(N) Time and Space
def findTheWinner(self, n: int, k: int) -> int:
    friends = [i for i in range(1, n + 1)]
    start = 0
    while len(friends) > 1:
        start = (start + k - 1) % len(friends) # it will be the next start as well, if we are removing from list.
        del friends[start]
    return friends[0]
