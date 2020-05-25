class TreeNode:
    def __init__(self, d):
        self.data = d
        self.next = None


def maxSum(root):
    traverse(root)


def traverse(root):
    if root is None:
        return [0, 0]

    p1 = traverse(root.left)
    p2 = traverse((root.right))
    l1 = max(p1[0], p2[0]) + root.data
    l2 = p1[1] + p2[1] + root.data
    maxs = max(l1,l2)
    return