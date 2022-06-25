import sys

def divide_mul(a,b,c):
  if b==0:
    return 1
  elif b==1:
    return a%c

  tmp=divide_mul(a,b//2,c)
  if b%2:
    return (tmp*tmp*a)%c
  else:
    return (tmp*tmp)%c

a,b,c=map(int,sys.stdin.readline().rstrip().split())


print(divide_mul(a,b,c))