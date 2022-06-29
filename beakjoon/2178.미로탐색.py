from collections import deque
import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
graph=[]
for _ in range(n):
  graph.append(list(map(int,list(sys.stdin.readline().rstrip()))))

queue=deque([[0,0]])

graph[0][0]=1
while queue:
  x,y=queue.popleft()
  
  #아래
  if x<n-1 and graph[x+1][y]==1:
    queue.append([x+1,y])
    graph[x+1][y]=graph[x][y]+1
  
  #왼쪽
  if y>0 and graph[x][y-1]==1:
    queue.append([x,y-1])
    graph[x][y-1]=graph[x][y]+1
    
  #위
  if x>0 and graph[x-1][y]==1:
    queue.append([x-1,y])
    graph[x-1][y]=graph[x][y]+1
    
  #오른쪽
  if y<m-1 and graph[x][y+1]==1:
    queue.append([x,y+1])
    graph[x][y+1]=graph[x][y]+1

print(graph[n-1][m-1])