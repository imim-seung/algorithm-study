import sys


n,k=map(int, sys.stdin.readline().rstrip().split())
coin_list=[]
for _ in range(n):
  coin_list.append(int(sys.stdin.readline().rstrip()))

coin_list.sort(reverse=True)
count=0
for c in coin_list:
  if c<=k:
    count+=k//c
    k=k%c
  if k<=0:
    break

print(count)