class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root):
        def check(a,b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val!=b.val:
                return False
            return check(a.left,b.right) and check(a.right,b.left)
        return check(root.left,root.right)

p=TreeNode(1)
p.left=TreeNode(2)
p.right=TreeNode(2)
p.left.left=TreeNode(2)
p.left.right=TreeNode(3)
p.right.left=TreeNode(3)
p.right.right=TreeNode(2)
s1=Solution()
print(s1.isSymmetric(p))