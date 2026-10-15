# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        def height(root):
            if not root: return 0
            left = height(root.left)
            right = height(root.right)
            return 1 + max(left,right)
        
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            if abs(height(node.left) - height(node.right)) > 1:
                return False

        return True

