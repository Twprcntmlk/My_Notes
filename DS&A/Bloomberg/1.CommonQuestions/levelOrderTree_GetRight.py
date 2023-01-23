# Time complexity : O(N) since each node is processed exactly once.
# Space complexity : O(N) to keep the output structure which contains N node values.

def levelOrder(root):
    queue=[root]
    result=[]

    while queue:
        level=[]
        for i in range(len(queue)):
            node=queue.pop(0)
            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        if level:
                result.append(level)
    return result
###################################################################################
def levelOrder(root):
    level_dict = dict()

    def get_nodes(root, level):
        if root:
            hold = level_dict.get(level, [])
            hold.append(root.val)
            level_dict[level] = hold
            get_nodes(root.left, level + 1)
            get_nodes(root.right, level + 1)
    get_nodes(root, 0)
    return [level_dict[x] for x in level_dict]
###################################################################################

#MAX at of EACH LEVEL

def solve(self, root):
    level = [(root, 0)] if root else []
    max_width = 0
    while level:
        max_width = max(max_width, level[-1][1] - level[0][1] + 1)
        next_level = []
        for node, x in level:
            if node.left:
                next_level.append((node.left, 2 * x))
            if node.right:
                next_level.append((node.right, 2 * x + 1))
        level = next_level
    return max_width

## LEFT MOST NODES
    def solve(self, root):
        result = [root.val]
        sameLevel = [root]
        while sameLevel:
            nextLevel = []
            for node in sameLevel:
                nextLevel += [node.left, node.right]
            nextLevel = [node for node in nextLevel if node]
            if nextLevel:
                result.append(nextLevel[0].val)
            sameLevel = nextLevel
        return result

### Sort Nodes in Tree
def sortNodes(root):
  queue = [(root, None)]

  while queue:
    queue = sorted(queue, key=lambda x : x[0].val)

    for _ in len(queue):
      node, parentNode  = queue.pop(0)

      if parentNode:
        parentNode.children.append(node)

      for child in node.children:
        queue.append((child, node))
      node.children = []

  return root
