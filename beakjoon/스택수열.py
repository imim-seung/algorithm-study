
import collections


from collections import deque

n=int(input())
num_list=deque()
stack=[]
state=[]
for _ in range(n):
  num_list.append(int(input()))


for i in range(1,n+1):
  stack.append(i)
  state.append('+')
  while stack and stack[-1]==num_list[0]:
    stack.pop()
    num_list.popleft()
    state.append('-')

if num_list:
  print("NO")
else:
  for s in state:
    print(s)


