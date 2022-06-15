import sys

n=int(sys.stdin.readline().rstrip())
people=list(map(int,sys.stdin.readline().rstrip().split()))

time=0
people.sort()
for i, p in enumerate(people):
  time+=p*(len(people)-i)


print(time)
