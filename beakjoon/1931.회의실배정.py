
import sys


n=int(sys.stdin.readline().rstrip())
booked=[]
for _ in range(n):
  booked.append(tuple(map(int,sys.stdin.readline().rstrip().split())))

booked.sort(key=lambda x : (x[1],x[0]))

now=0
count=0
for start,end in booked:
  if start>=now:
    count+=1
    now=end

print(count)

