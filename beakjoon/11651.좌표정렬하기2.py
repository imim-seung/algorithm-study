import sys

n=int(sys.stdin.readline().rstrip())
location=[]
for _ in range(n):
    x,y=map(int, sys.stdin.readline().rstrip().split())
    location.append((x,y))

location.sort(key=lambda x : (x[1],x[0]))

for x,y in location:
    print(str(x)+' '+str(y))


