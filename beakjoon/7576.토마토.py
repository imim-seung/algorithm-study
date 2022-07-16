from collections import deque
import sys

# def bfs(graph, visited, startX, startY):
# visited[startX][startY]=True

m,n=map(int,sys.stdin.readline().rstrip().split())
graph=[]
for _ in range(n):
  graph.append(list(map(int,sys.stdin.readline().rstrip().split())))

q=deque()
count=0
visited=[[False]*m for _ in range(n)]
X=[0,0,-1,1]
Y=[-1,1,0,0]

#시작노트 탐색
for j in range(n):
  for k in range(m):
    if graph[j][k] == 1 and not visited[j][k]:
      visited[j][k]=True
      q.append([j,k,0])

while q :
  node=q.popleft()
  for l in range(4):
    x=node[0]+X[l]
    y=node[1]+Y[l]
    if x>=0 and x<n and y >=0 and y<m and graph[x][y]==0:
      visited[x][y]=True
      graph[x][y]=1
      q.append([x,y,node[2]+1])
      count=max(node[2]+1,count)

for j in range(n):
  for k in range(m):
    if graph[j][k] ==0:
      print(-1)
      sys.exit()

print(count)
  




          
      





