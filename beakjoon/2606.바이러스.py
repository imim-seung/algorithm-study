import sys

computer=int(sys.stdin.readline().rstrip())

graph=[[] for _ in range(computer+1)]

edge=int(sys.stdin.readline().rstrip())

for _ in range(edge):
  a,b=map(int,sys.stdin.readline().rstrip().split())
  graph[a].append(b)
  graph[b].append(a)

stack=[1]
worm_set=set()

while stack:
  c=stack.pop()
  worm_set.add(c)
  while graph[c]:
    stack.append(graph[c].pop())

print(len(worm_set)-1)



