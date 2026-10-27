class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # we want to determine existence of a single word 
        # start at root node, run dfs. note that we will hav a cycle present, as each charcter is not directed
        # iterate through the board and search for the starting character of our word. 
        # if it exists, run dfs and check for the next character. recurse.
        # we must add in a visited set to prevent recursing onto an already visited node
        row_len = len(board[0])
        col_len = len(board)
        visited = set()

        def dfs(row, col, index):
            if (row,col) in visited or row < 0 or row >= col_len or col >= row_len or col < 0:
                return False
            if board[row][col] != word[index]:
                return False
            visited.add((row,col))
            if index+1 == len(word):
                return True
            if dfs(row-1,col,index+1):
                return True
            if dfs(row+1,col,index+1):
                return True
            if dfs(row,col+1,index+1):
                return True
            if dfs(row,col-1,index+1):
                return True
            # This line solves the previous visited node blocking the way problem
            visited.remove((row,col))
            return False

        for i in range(col_len):
            for j in range(row_len):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
                    visited.clear()
        return False
