# Time Comp: O(n^2)
# Space Comp: O(n)
from collections import defaultdict
def unhappyFriends( n, preferences, pairs):

        pairing={}
        for i,j in pairs:
            pairing[i]=set(preferences[i][:preferences[i].index(j)])
            pairing[j]=set(preferences[j][:preferences[j].index(i)])
        #create dictionary of people who i prefer more.

        # I want to find if i prefer them more and they prefer me more
        #if they are in MY more preferred and if I and in there more preferred, then UNHAPPY
        unhappy=0
        for key in pairing:
            for friends in preferences[key]:
                if key in preferences[friends]:
                    unhappy+=1
                    break # so we don't count multiple times
        return unhappy

# n = 4
# preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]]
# pairs = [[1, 2], [0, 3]]
# print(unhappyFriends(n, preferences, pairs))
