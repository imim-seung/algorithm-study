from collections import deque
import sys
test_case=int(sys.stdin.readline().rstrip())

for _ in range(test_case):
  printer=deque()
  p_out=[]
  len, target=map(int, sys.stdin.readline().rstrip().split())
  for index, priority in enumerate(sys.stdin.readline().rstrip().split()):
    printer.append((index,int(priority)))
  while printer:
    max_p=max(i[1] for i in printer)
    while printer[0][1] !=max_p:
      printer.rotate(-1)
    p_out.append(printer.popleft()[0])
  print(p_out.index(target)+1)

