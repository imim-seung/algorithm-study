import sys
sys.setrecursionlimit(10**6)


def dfs(graph, visited,v):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,visited,i)
    return visited
    
n,m=map(int, sys.stdin.readline().rstrip().split())

graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(m):
    u,v=map(int , sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

visited[0]=True
count=0
v=1

while False in visited:
    count+=1
    visited=dfs(graph,visited,v)
    for i, visit in enumerate(visited):
        if not visit:
            v=i
            break

print(count)
