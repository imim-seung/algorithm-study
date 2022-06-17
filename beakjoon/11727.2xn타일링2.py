import sys

tile=[0]*1001
n=int(sys.stdin.readline().rstrip())
for i in range(1,n+1):
  if i==1:
    tile[i]=1
  elif i==2:
    tile[i]=3
  else:
    tile[i]=tile[i-1]+(tile[i-2]*2)

print(tile[n]%10007)


