from collections import deque
import sys

n=int(sys.stdin.readline().rstrip())
graph=[]
visited=[[False]*n for _ in range(n)]
q=deque()
apart_c=[]

for _ in range(n):
  graph.append(list(map(int,list(sys.stdin.readline().rstrip()))))

number=0
dx=[0,0,-1,1]
dy=[-1,1,0,0]
for i in range(n):
  for j in range(n):
    if graph[i][j]==1 and not visited[i][j]:
      visited[i][j]=True
      q.append([i,j])
      number+=1
      count=1
      while q:
        node=q.popleft()
        for k in range(4):
          x=dx[k]+node[1]
          y=dy[k]+node[0]
          if x>=0 and y >=0 and x<n and y<n and graph[y][x]==1 and not visited[y][x]:
            visited[y][x]=True
            q.append([y,x])
            count+=1
      apart_c.append(count)

print(number)
apart_c.sort()
for a in apart_c:
  print(a)




        




