import sys
def fac(n):
  if n==1 or n==0:
    return 1
  else :
    return n*fac(n-1)

n, k=map(int, sys.stdin.readline().rstrip().split())

print(fac(n)//(fac(k)*fac((n-k))))