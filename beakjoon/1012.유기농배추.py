from collections import deque
import sys

test_case=int(sys.stdin.readline().rstrip())
for _ in range(test_case):

  m,n,k=map(int , sys.stdin.readline().rstrip().split())

  field=[[0]*m for _ in range(n)]
  visited=[[False]*m for _ in range(n)]

  for _ in range(k):
    x,y = map(int , sys.stdin.readline().rstrip().split())
    field[y][x]=1

  dx=[-1,1,0,0]
  dy=[0,0,-1,1]
  queue=deque()
  count=0

  for s in range(n):
    for t in range(m):
      if field[s][t]==1 and not visited[s][t]:
        queue.append([s,t])
        visited[s][t]=True
        count+=1    
      while queue:
        node=queue.popleft()
        for a in range(4):
          i=node[0]+dx[a]
          j=node[1]+dy[a]
          if i >=0 and j>=0 and i<n and j<m and field[i][j]==1 and not visited[i][j]:
            queue.append([i,j])
            visited[i][j]=True
      
  print(count)

