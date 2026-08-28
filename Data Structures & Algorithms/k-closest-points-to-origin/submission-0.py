import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist={}
        heap=[]
        for i,point in enumerate(points):
            dist[i]=math.sqrt(point[0]**2+point[1]**2)
        for i,point in enumerate(points):
            heapq.heappush(heap,(-dist[i],point))
        while(len(heap)!=k):
            heapq.heappop(heap)
        return [x[1] for x in heap] 