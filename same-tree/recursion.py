# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q):
        def inorder(root):
            res = []

            if not root:
                res.append(None)
                print(res)
                return res

            res.append(root.val)
            print(res)
            res += inorder(root.left)
            res += inorder(root.right)
            print(res)
            return res

        return inorder(p) == inorder(q)

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

solution = Solution()

print(solution.isSameTree(p, q))