# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        q = deque([])
        q.append(root)
        def dfs(node,targetNode):
            if not node and not targetNode:
                return True
            if not node and targetNode:
                return False
            if not targetNode and node:
                return False
            if targetNode.val != node.val:
                return False
            else:
                return dfs(node.left,targetNode.left) and dfs(node.right, targetNode.right)



        def bfs_start():
            while q:
                cur = q.popleft()
                if cur.val == subRoot.val and dfs(cur,subRoot):
                    return True
                
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            return False
            
            

            

        
            

        return bfs_start()

            
