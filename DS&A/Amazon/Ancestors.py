# parent_child_pairs = [
#     (5, 6), (1, 3), (2, 3), (3, 6), (15, 12),
#     (5, 7), (4, 5), (4, 9), (9, 12), (30, 16)
# ]

# from collections import defaultdict;
# def find_nodes_with_zero_and_one_parents(parent_child_pairs):
#     adjList=defaultdict(list)
#     allNodes =set()

#     oneParent = []
#     zeroParent = []

#     for x,y in parent_child_pairs:
#         adjList[y].append(x)

#     for x,y in parent_child_pairs:
#         allNodes.add(x)
#         allNodes.add(y)

#     for num in allNodes:
#         if num not in adjList:
#             zeroParent.append(num)
#         if len(adjList[num]) == 1:
#             oneParent.append(num)

#     return [zeroParent,oneParent]
# #[zeroParent,oneParent]
# #[[1, 2, 4, 15, 30], [5, 7, 9, 16]]
# # zeroParents = not in key
# # has 1 child:

# print(find_nodes_with_zero_and_one_parents(parent_child_pairs))
####################################################################################
"""
Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique positive integer identifier.

For example, in this diagram, 6 and 8 have common ancestors of 4 and 14.

               15
              / \
         14  13  21
         |   |
1   2    4   12
 \ /   / | \ /
  3   5  8  9
   \ / \     \
    6   7     11

parent_child_pairs_2 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (15, 21), (4, 8), (4, 9), (9, 11), (14, 4), (13, 12),
    (12, 9), (15, 13)
]

Write a function that takes this data and the identifiers of two individuals as inputs and returns true if and only if they share at least one ancestor.

Sample input and output:

has_common_ancestor(parent_child_pairs_2, 3, 8)   => false
has_common_ancestor(parent_child_pairs_2, 5, 8)   => true
has_common_ancestor(parent_child_pairs_2, 6, 8)   => true
has_common_ancestor(parent_child_pairs_2, 6, 9)   => true
has_common_ancestor(parent_child_pairs_2, 1, 3)   => false
has_common_ancestor(parent_child_pairs_2, 3, 1)   => false
has_common_ancestor(parent_child_pairs_2, 7, 11)  => true
has_common_ancestor(parent_child_pairs_2, 6, 5)   => true
has_common_ancestor(parent_child_pairs_2, 5, 6)   => true
has_common_ancestor(parent_child_pairs_2, 3, 6)   => true
has_common_ancestor(parent_child_pairs_2, 21, 11) => true

n: number of pairs in the input


"""
from collections import defaultdict;
parent_child_pairs_2 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (15, 21),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9),
    (15, 13)
]

def has_common_ancestor(parent_child_pairs_2, num1, num2):
    adjList=defaultdict(list)

    for x,y in parent_child_pairs_2:
        adjList[y].append(x)
    ancestors1 = None
    ancestors2 = None

    def dfs(node, person, arr):
        nonlocal ancestors1
        nonlocal ancestors2
        if node not in adjList:
            if person == 1:
                ancestors1 = arr
            else:
                ancestors2 = arr
        # print(arr)
        for child in adjList[node]:

            dfs(child, person, arr+[child])

    dfs(num1,1,arr=[])
    dfs(num2,2,arr=[])

    for x in ancestors1:
        if x in ancestors2:
            return True
    return False

for x,y in [(4,6)]: #(1,3),(3,1),(4,6),(8,5)
    print(has_common_ancestor(parent_child_pairs_2, x,y))
