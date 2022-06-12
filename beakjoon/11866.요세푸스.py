from collections import deque
import sys 


n,k=map(int, sys.stdin.readline().rstrip().split())
queue=deque()
pop_list=[]
for i in range(1,n+1):
  queue.append(i)

while queue:
  queue.rotate(-(k-1))
  pop_list.append(queue.popleft())

print('<'+', '.join(map(str,pop_list))+'>')
