class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = set()
        island_arr = []

        # implement bfs
        def bfs(r, c, island):
            # iteratively!
            queue = deque([[r,c]])
            while queue:
                curr_node = queue.popleft()
                # if out of bounds skip
                if curr_node[0]<0 or curr_node[1]<0 or curr_node[0]>=row or curr_node[1]>=col:
                    continue
                # if node is not 1 or already visited skip
                if grid[curr_node[0]][curr_node[1]]=="0" or tuple(curr_node) in visited:
                    continue
                island.append(curr_node)
                visited.add(tuple(curr_node))
                queue.append([curr_node[0]+1,curr_node[1]])
                queue.append([curr_node[0]-1,curr_node[1]])
                queue.append([curr_node[0],curr_node[1]+1])
                queue.append([curr_node[0],curr_node[1]-1])
            return

        for r in range(row):
            for c in range(col):
                # if a node is 0 or visited, skip
                if (r,c) in visited or grid[r][c]=="0":
                    continue
                else:
                    #run bfs iteratively. 
                    # This is to counter recursion depth error in python
                    island = []
                    # our bfs will mutate the island array into a group of nodes
                    bfs(r,c, island)
                    island_arr.append(island)
        return len(island_arr)