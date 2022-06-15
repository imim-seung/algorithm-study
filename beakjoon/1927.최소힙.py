import heapq
import sys

n=int(sys.stdin.readline().rstrip())
heap=[]

for _ in range(n):
  command=int(sys.stdin.readline().rstrip())
  if command >0:
    heapq.heappush(heap,command)
  else:
    if heap:
      print(heapq.heappop(heap))
    else:
      print(0)


