import sys

n=int(sys.stdin.readline().rstrip())

for i in range(1000002):
  
  if sum(map(int,list(str(i))))+i ==n:
    print(i)
    break
  if i>n:
    print(0)
    break


