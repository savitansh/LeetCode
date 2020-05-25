class TreeNode:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.moves = 0

    def distributeCoins(self, root: TreeNode) -> int:
        v = self.traverse(root)
        if abs(v) > 0:
            self.moves += abs(v)
        return self.moves

    def traverse(self, root):
        if root is None:
            return 0
        l = self.traverse(root.left)
        r = self.traverse(root.right)
        l1 = abs(l)
        l2 = abs(r)
        if l1 + l2 > 0:
            self.moves += l1 + l2
        return l + r + 1 - root.val


if __name__ == '__main__':
    inst = Solution()
    root = TreeNode(0)
    l1 = TreeNode(3)
    root.left = l1
    l2 = TreeNode(0)
    root.right = l2
    print(inst.distributeCoins(root))
