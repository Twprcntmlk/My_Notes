class Leaderboard:
    from collections import defaultdict;
    def __init__(self):
        self.scoreBoard=defaultdict()
    # O(1) for addScore.
    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scoreBoard:
              self.scoreBoard[playerId]=0
        self.scoreBoard[playerId]+=score
    # O(NlogN) total number of players + sort
    def top(self, K: int) -> int:
        values = list(self.scoreBoard.values())
        return sum(sorted(values, reversed=True)[:K])
    # O(1) for reset.
    def reset(self, playerId: int) -> None:
           self.scoreBoard[playerId]
#############################################################################
class Leaderboard:
    def __init__(self):# O(1)
        self.table = Counter()# O(N) dict

    def addScore(self, playerId: int, score: int) -> None:
        self.table[playerId] += score

    def top(self, K: int) -> int: # O(N)
        return sum(x for _, x in self.table.most_common(K))

    def reset(self, playerId: int) -> None:# O(1)
        self.table.pop(playerId)
