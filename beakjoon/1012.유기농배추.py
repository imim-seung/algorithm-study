from collections import deque
import sys

test_case=int(sys.stdin.readline().rstrip())
for _ in range(test_case):

  m,n,k=map(int , sys.stdin.readline().rstrip().split())

  field=[[0]*m for _ in range(n)]

  for _ in range(k):
    y,x = map(int , sys.stdin.readline().rstrip().split())
    field[x][y]=1

  dx=[-1,1,0,0]
  dy=[0,0,-1,1]
  count=0
  queue=deque()

  for s in range(n):
    for t in range(m):
      if field[s][t]==1:
        queue.append([s,t])    
        while queue:
          i,j=queue.popleft()
          for a in range(4):
            i+=dx[a]
            j+=dy[a]
            if i >=0 and j>=0 and i<m and j < n:
              queue.append([i,j])
              field[i][j]=0
        count+=1
  print(count)

