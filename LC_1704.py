def inorder(root, l, r, ans):
    if root is None:
        return
    inorder(root.left, l, r)
    if l <= root.data <= r:
        ans.append(root.data)
    inorder(root.right, l, r, ans)


def rangeSumBST(root, L, R):
    ans = []
    inorder(root, L, R, ans)
    return sum(ans)
