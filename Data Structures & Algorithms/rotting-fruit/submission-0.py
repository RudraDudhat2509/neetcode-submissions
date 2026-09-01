from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        g=deepcopy(grid)

        fresh=0
        min=0

        q=deque() 

        for i in range(row):
            for j in range(col):
                if(g[i][j]==2):
                    q.append((i,j))
                elif(g[i][j]==1):
                    fresh+=1
        
        while len(q)!=0 and fresh>0:
            min+=1
            rotten=len(q)
            for _ in range(rotten):
                i,j=q.popleft()
                for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                    newi=i+dx
                    newj=j+dy
                    if(newi<0 or newj<0 or newi==row or newj==col):
                        continue 
                    if(g[newi][newj]==0 or g[newi][newj]==2 ):
                        continue 
                    g[newi][newj]=2
                    q.append((newi,newj))
                    fresh-=1
        if fresh>0: 
            return -1
        return min