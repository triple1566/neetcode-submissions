class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = len(board)
        # 1. We will check duplicates in the row
        row_map = {}
        for row in range(length):
            row_map[row] = []
            for col in range(length):
                if board[row][col]==".":
                    continue
                if board[row][col] in row_map[row]:
                    return False
                else:
                    row_map[row].append(board[row][col])
        # ---> O(N^2)

        # 2. We will check duplicates in the columns
        col_map = {}
        for col in range(length):
            col_map[col] = []
            for row in range(length):
                if board[row][col]==".":
                    continue
                if board[row][col] in col_map[col]:
                    return False
                else:
                    col_map[col].append(board[row][col])
        # ---> O(N^2)

        # 3. We will check duplicates in the sections
        sec_map = {}
        for row in range(length):
            for col in range(length):
                if board[row][col]==".":
                    continue
                if (int(row/3),int(col/3)) not in sec_map:
                    sec_map[(int(row/3),int(col/3))] = []
                if board[row][col] in sec_map[(int(row/3),int(col/3))]:
                    return False
                else:
                    sec_map[(int(row/3),int(col/3))].append(board[row][col])
        
        return True