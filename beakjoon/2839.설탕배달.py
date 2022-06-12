import sys

n=int(sys.stdin.readline().rstrip())

for i in range(n//3+1):
  for j in range(n//5+1):
    total= 5 * j + 3 * i
    if total==n:
      print(i+j)
      sys.exit()
print(-1)