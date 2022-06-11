import sys
n=int(sys.stdin.readline().rstrip())
members=[]

for i in range(n):
    age, name=sys.stdin.readline().rstrip().split()
    members.append((int(age),i,name))

members.sort(key=lambda x : (x[0],x[1]))

for m in members:
    print(m[0], end=' ')
    print(m[2])
