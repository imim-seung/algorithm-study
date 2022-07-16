from collections import deque
import sys



m,n,h=map(int,sys.stdin.readline().rstrip().split())
graph=[]
for _ in range(h):
  box=[]
  for _ in range(n):
    box.append(list(map(int,sys.stdin.readline().rstrip().split())))
  graph.append(box)

q=deque()
count=0
visited=[[[False]*m for _ in range(n)] for _ in range(h)]
X=[0,0,-1,1,0,0]
Y=[-1,1,0,0,0,0]
Z=[0,0,0,0,-1,1]

#시작노트 탐색
for i in range(h):
  for j in range(n):
    for k in range(m):
      if graph[i][j][k] == 1 and not visited[i][j][k]:
        visited[i][j][k]=True
        q.append([i,j,k,0])

while q :
  node=q.popleft()
  for l in range(6):
    z=node[0]+Z[l]
    y=node[1]+Y[l]
    x=node[2]+X[l]
    if x>=0 and x<m and y >=0 and y<n and z>=0 and z<h and graph[z][y][x]==0:
      visited[z][y][x]=True
      graph[z][y][x]=1
      q.append([z,y,x,node[3]+1])
      count=max(node[3]+1,count)
for i in range(h):
  for j in range(n):
    for k in range(m):
      if graph[i][j][k] ==0:
        print(-1)
        sys.exit()

print(count)
  




          
      





