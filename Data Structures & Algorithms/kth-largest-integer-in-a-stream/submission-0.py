class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums
        self.heap=[]
        for i in nums:
            heapq.heappush(self.heap,i)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        self.clone=self.heap
        while(len(self.clone)!=self.k):
            heapq.heappop(self.clone)
        return self.clone[0]