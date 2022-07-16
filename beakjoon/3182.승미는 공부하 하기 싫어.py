import sys

n=int(sys.stdin.readline().rstrip())
graph=[]
stack=[]
count_list=[]



for i in range(n):
  graph.append(int(sys.stdin.readline().rstrip())-1)

#시작노드를 찾는다.
for i in range(n):
  count=0
  visited=[False]*n
  visited[i]=True
  stack.append(graph[i])
  while stack:
    count+=1
    v=stack.pop()
    if not visited[v]:
      visited[v]=True
      stack.append(graph[v])
  count_list.append([count,i])

count_list.sort(key=lambda x : (-x[0],x[1]))

print(count_list[0][1]+1)

  


