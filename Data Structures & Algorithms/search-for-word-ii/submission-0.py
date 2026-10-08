class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.idx = -1
        self.refs = 0
    
    def addWord(self, word, i):
        curr = self
        curr.refs += 1
        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
            curr.refs += 1
        curr.idx = i

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for i in range(len(words)):
            root.addWord(words[i], i)
        
        rows, cols = len(board), len(board[0])
        res = []

        def getIndex(c):
            index = ord(c) - ord('a')
            return index
        
        def dfs(r, c, node):
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] == '*' or not node.children[getIndex(board[r][c])]):
                return 0
            
            temp = board[r][c]
            board[r][c] = '*'
            prev = node
            node = node.children[getIndex(temp)]
            found = 0
            if node.idx != -1:
                res.append(words[node.idx])
                node.idx = -1
                found += 1
            
            found += dfs(r + 1, c, node)
            found += dfs(r - 1, c, node)
            found += dfs(r, c + 1, node)
            found += dfs(r, c - 1, node)

            board[r][c] = temp
            node.refs -= found
            if not node.refs:
                prev.children[getIndex(temp)] = None
            return found
        
        for r in range(rows):
            for c in range(cols):
                root.refs -= dfs(r, c, root)
        
        return res