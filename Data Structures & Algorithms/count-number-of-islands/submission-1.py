class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #1 <= grid.length, grid[i].length <= 100
        #grid[i][j] is '0' or '1'.


        # iterate through all 1-vertex in the matrix (skip the ones already bound by an island)
        # for each 1-vertex that are not already in the island list, dfs and determine all connected nodes.
        # add the island in the island list along with all connected nodes.
        # return the length of our island list

        # since we need to store the coords in our island list, lets use range iteration

        # Lets define a helper function to determine if a node is in the island list.
        island_arr = []
        visited = set()
        # The length variables to avoid calling length every time we check for boundary errors
        col = len(grid[0])
        row = len(grid)

        # Now lets implement our dfs function
        # our dfs will take a list representing a single island, and append correct nodes to the list recursively.
        def dfs(r,c,island):
            if r<0 or c<0 or r>=row or c>=col:
                # out of bounds
                return
            if grid[r][c]!="1":
                # not an island node
                return
            if (r,c) in visited:
                #node already visited
                return
            # add our node to the island as it is correct and not visited.
            island.append([r,c])
            visited.add(tuple([r,c]))
            # run dfs for each adjacent nodes
            for node in [[r-1,c],[r+1,c],[r,c-1],[r,c+1]]:
                dfs(node[0],node[1],island)
            return

        for r in range(row):
            for c in range(col):
                # For each node, check if:
                # node is 1, node is not already in the island list
                if grid[r][c] == "1" and (r,c) not in visited:
                    # run dfs
                    island=[]
                    dfs(r,c,island)
                    island_arr.append(island)
                else:
                    continue
        
        return len(island_arr)
        


