class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap, self.k = nums, k
        heapq.heapify(self.heap)
        # this is a minheap. we will pop until we only have k elements in our heap.
        while len(self.heap) > k :
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        if len(self.heap) == 0:
            heapq.heappush(self.heap,val)
        elif val > self.heap[0]:
            heapq.heappush(self.heap, val)
        while len(self.heap) > self.k :
            heapq.heappop(self.heap)
        return self.heap[0]

