class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

def solution(root):
    word = None

    def dfs(root, curr):
        if not root:
            word = min(word, curr)
            return

        for child in root.children:
            dfs(child, root.val + curr)

    dfs(root)
    return word
