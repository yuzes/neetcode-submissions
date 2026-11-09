# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res = 0
        q = deque()
        # q stores 
        if root:
            q.append((root, float("-inf")))
        while q:
            node, maxSoFar = q.popleft()
            if maxSoFar <= node.val:
                maxSoFar = node.val
                res += 1
            if node.left:
                q.append((node.left, maxSoFar))
            if node.right:
                q.append((node.right,maxSoFar))
        return res

        