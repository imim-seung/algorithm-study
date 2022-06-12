import sys


a,b,v=map(int,sys.stdin.readline().rstrip().split())
now=0
days=0
while now < v:
  days+=1
  now+=a
  if now>=v:
    print(days)
    sys.exit()


    
  now-=b




