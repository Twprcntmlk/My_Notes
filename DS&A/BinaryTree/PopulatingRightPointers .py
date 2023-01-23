def connect(root):
    if root:
        # if it's not a leaf node
        if root.left and root.right:
            # connect the left child to the right child
            root.left.next = root.right
            # if the current node has the next set
            if root.next:
                # the current right's next will be the left child of it
                root.right.next = root.next.left
            # repeat the process recursevely
            self.connect(root.left)
            self.connect(root.right)

    return root
