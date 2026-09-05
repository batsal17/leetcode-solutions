class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        res=[]
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res

root = TreeNode(1)
root.left = None
root.right = TreeNode(2)
root.right.left = TreeNode(3)


s1 = Solution()
print(s1.inorderTraversal(root))