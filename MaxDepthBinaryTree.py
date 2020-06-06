# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(node):
    """
    :type node: TreeNode
    :rtype: int
    """
    if node is None:
        return 0
    else:
        ldepth = max_depth(node.left)
        rdepth = max_depth(node.right)

    if ldepth > rdepth:
        return ldepth + 1
    else:
        return rdepth + 1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.right = TreeNode(6)
root.right.left = TreeNode(7)

print "maxdepth is : " + str(max_depth(root))
