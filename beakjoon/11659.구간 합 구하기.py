import sys

n,m=map(int, sys.stdin.readline().rstrip().split())
num_list=list(map(int, sys.stdin.readline().rstrip().split()))
sum_list=[0]*(n+1)

for a in range(n):
    if a==0:
      sum_list[a]=num_list[0]
    else:
      sum_list[a]=num_list[a]+sum_list[a-1]

for _ in range(m):
  i,j=map(int, sys.stdin.readline().rstrip().split())
  if i==1:
    print(sum_list[j-1])
  else : 
    print(sum_list[j-1]-sum_list[i-2])


