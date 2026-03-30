class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]

        cur.word = word
    
    def search(self,word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            else:
                cur = cur.children[char]
        return cur.word
    
    def prefixsearch(self,prefix):
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            else:
                cur = cur.children[char]
        return True
    


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #create a prefix tree for words
        #dfs and keep track of the current string and search if its in the tree
        word_tree = PrefixTree()
        for word in words:
            word_tree.insert(word)
        neighbors = [(0,1),(1,0),(-1,0),(0,-1)]
        res = []

        def dfs(row,col,seen,cur_word):
            cur_word = cur_word + board[row][col]
            seen.add((row,col))
            if word_tree.search(cur_word) and cur_word not in res:
                res.append(cur_word)
                
            if word_tree.prefixsearch(cur_word):
                for nr,nc in neighbors:
                    newrow = row + nr
                    newcol = col + nc
                    if newrow < 0 or newcol < 0 or newrow >= len(board) or newcol >= len(board[0]) or (newrow,newcol) in seen:
                        continue
                        
                    else:
                        dfs(newrow,newcol,seen,cur_word)
            
            seen.remove((row,col))

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in word_tree.root.children:
                    dfs(r,c,seen = set(),cur_word = "")
                

        return res



        