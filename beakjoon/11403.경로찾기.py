from collections import deque
import sys

def serch(graph,visited,start, end):
  q=deque([start])
  while q:
    node=q.popleft()
    visited[node]=True
    for i, v in enumerate(graph[node]):
      if v == 1:
        if i == end : 
          return True
        if not visited[i]:
          q.append(i)
  return False

n=int(sys.stdin.readline().rstrip())
graph=[]

for _ in range(n):
  graph.append(list(map(int,sys.stdin.readline().rstrip().split())))

for i in range(n):
  for j in range(n):
    visited=[False]*n
    if serch(graph,visited,i,j):
      print(1,end=' ')
    else:
      print(0, end=' ')
  print()




