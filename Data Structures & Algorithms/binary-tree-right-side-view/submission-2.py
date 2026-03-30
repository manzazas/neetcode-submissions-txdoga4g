# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #Traverse the tree in level order
        #keep track of each level in a list, only append the right most node

        res = []

        def bfs(node):
            queue = deque()
            if node:
                queue.append(node)
            while queue:
                level_list = []
                for i in range(len(queue)):
                    cur = queue.popleft()
                    level_list.append(cur.val)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                res.append(level_list[-1])
        
        bfs(root)
        return res

            


        