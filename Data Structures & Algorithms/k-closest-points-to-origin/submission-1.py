class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points)==k:
            return points
        #How should I heapify my matrix
        # ===> This is NOT a matrix, it is merely a list of points!
        # loop over all indices in the matrix -> calculate distance and store it alongside the coordinate data as a tuple -> heapify the array of tuple, and pop the heap until we have k length
        heap = []
        # Note that this part has an n^2 time complexity
        for coord in points:
            dist = math.sqrt(math.pow(coord[0],2) + math.pow(coord[1],2))
            # reverse sign for dist values to simulate maxheap
            heap.append((-dist,coord))
        
        # At this point in runtime we should have a heapifiable array of distance and list.
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        # since we want closest points, we should use maxheap, as maxheap will pop the maximum values.
        res=[]
        for i in range(0,k):
            res.append(heap[i][1])
        return res