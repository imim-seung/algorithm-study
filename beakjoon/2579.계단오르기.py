import sys

n=int(sys.stdin.readline().rstrip())
stairs=[]
d=[0]*n

for _ in range(n):
  stairs.append(int(sys.stdin.readline().rstrip()))


for i  in range(n):
  if i==0:
    d[i]=stairs[i]
  elif i ==1:
    d[i]=max(stairs[i],stairs[i-1]+stairs[i])
  elif i==2:
    d[i]=max(stairs[i-2]+stairs[i],stairs[i-1]+stairs[i])
  else:
    d[i]=max(stairs[i-1]+stairs[i]+d[i-3],stairs[i]+d[i-2])

print(d[-1])

