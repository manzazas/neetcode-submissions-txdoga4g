# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Level order means breadth first search
        #Return a list of lists
        #We need to keep track of each level
        res = []
        if not root:
            return res
        
        def bfs(root):
            queue = deque()
            if root:
                queue.append(root)

            while len(queue) > 0:
                level_list = []
                for i in range(len(queue)):
                    curr = queue.popleft()
                    level_list.append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                res.append(level_list)

            
        bfs(root)
        return res



            


