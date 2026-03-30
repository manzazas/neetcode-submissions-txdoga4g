# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([])
        q.append(root)
        depth = 0
        while q:
            for i in range(0,len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            depth += 1
        return depth
                


        #add the root to the queue. for each layer, add all the children to the queue. iterate a counter each time you do this. the final count is the max depth

            

        