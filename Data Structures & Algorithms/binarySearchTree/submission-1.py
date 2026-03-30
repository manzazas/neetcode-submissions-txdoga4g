class TreeNode:
    def __init__(self,key:int, val:int):
        self.key = key
        self.val = val
        self.left =None
        self.right = None



class TreeMap:
    
    def __init__(self):
        self.root =None
        
    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key,val)
        if self.root == None:
            self.root = newNode
            return
        
        cur = self.root
        while cur:
            if key < cur.key:
                if cur.left == None:
                    cur.left = newNode
                cur = cur.left
                
            elif key > cur.key:
                if cur.right == None:
                    cur.right = newNode
                cur = cur.right
            else:
                cur.val = val
                return
            
                



    def get(self, key: int) -> int:
        if not self.root:
            return -1
        cur = self.root

        while cur:
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                return cur.val
        return -1






    def getMin(self) -> int:
        if not self.root:
            return -1
        cur = self.root
        while cur and cur.left:
            cur = cur.left
        return cur.val



    def getMax(self) -> int:
        if not self.root:
            return -1
        cur = self.root
        while cur and cur.right:
            cur = cur.right
        return cur.val


    def remove(self, key: int) -> None:
        #traverse, find node. set the node value to one child, then delete the child
        
        def deleteNode(node, key):
            if not node:
                return None
            if key < node.key:
                node.left = deleteNode(node.left, key)
            elif key > node.key:
                node.right = deleteNode(node.right, key)
            else:
                # Node to delete found
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                # Both children exist
                # Find in-order successor (smallest in right subtree)
                succ = node.right
                while succ.left:
                    succ = succ.left
                node.key, node.val = succ.key, succ.val
                node.right = deleteNode(node.right, succ.key)
            return node

        self.root = deleteNode(self.root, key)
    def getInorderKeys(self) -> List[int]:

        
        res= []
        if not self.root:
            return res
        def inOrder(node):
            if not node:
                return None
            inOrder(node.left)
            res.append(node.key)
            inOrder(node.right)
        inOrder(self.root)
        return res


