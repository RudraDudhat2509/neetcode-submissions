class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for i in dic:
            heapq.heappush(heap,(dic[i],i))
        while(len(heap)!=k):
            heapq.heappop(heap)
        return [x[1] for x in heap]
