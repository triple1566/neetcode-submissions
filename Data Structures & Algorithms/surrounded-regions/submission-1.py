class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Condition for a region to be surrounded:
        # No "0" cells connected to an island is located on the edge of the board.

        # Initial Solution (This was wrong on bigger test cases):
        # Recurses through the nodes on the board, and run dfs on nodes that are marked "0" and is unvisited.
        # dfs() will return a boolean value based on the child recursive step is connected to an edge board.
        # Every recursive step, based on the bool vlue returned by dfs, determine whether to mark the node "X" or not.

        # Better solution:
        # Use BFS on every node that is already on the outer edge, and mark connected nodes as non_surrounded. 
        # next, go over all nodes and mark them 'X' if they are not in the non-surrounded set

        m = len(board)
        n = len(board[0])

        # BFS approach
        not_surrounded = set()
        BFS_visited = set()
        # def bfs here
        def bfs(r,c):
            queue = deque([[r,c]])
            while queue:
                curr_node = queue.popleft()
                if curr_node[0]<0 or curr_node[1]<0 or curr_node[0]>=m or curr_node[1]>=n:
                    continue
                if board[curr_node[0]][curr_node[1]]=='X' or (curr_node[0], curr_node[1]) in BFS_visited:
                    continue
                else:
                    BFS_visited.add(tuple(curr_node))
                    not_surrounded.add((curr_node[0], curr_node[1]))
                queue.append([curr_node[0]+1, curr_node[1]])
                queue.append([curr_node[0]-1, curr_node[1]])
                queue.append([curr_node[0], curr_node[1]-1])
                queue.append([curr_node[0], curr_node[1]+1])
        # run bfs on each outermost 0 marked node
        # left and right column
        for r in range(m):
            for c in [0,n-1]:
                if board[r][c] == 'O' and (r,c) not in BFS_visited:
                    bfs(r,c)
        for c in range(n):
            for r in [0,m-1]:
                if board[r][c] == 'O' and (r,c) not in BFS_visited:
                    bfs(r,c)
        # after this point, not_surrounded will contain every non-surrounded nodes in the board
        for r in range(m):
            for c in range(n):
                if (r,c) not in not_surrounded:
                    if board[r][c] == 'O':
                        board[r][c] = 'X'
        

