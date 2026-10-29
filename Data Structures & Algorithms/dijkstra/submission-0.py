class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # construct adjacency list for bfs
        adj = {}
        for i in range(n):
            adj[i] = []
        for s, d, weight in edges:
            adj[s].append([d,weight])

        # the {node : shortest path} hashmap relation
        shortest={}
        minheap = [(0,src)]
        heapq.heapify(minheap)
        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in shortest:
                continue
            shortest[n1] = w1
            for n2, w2 in adj[n1]:
               if n2 not in shortest:
                    heapq.heappush(minheap, [w1+w2, n2])
        
        for i in range(n):
            if i not in shortest:
                shortest[i]=-1

        return shortest