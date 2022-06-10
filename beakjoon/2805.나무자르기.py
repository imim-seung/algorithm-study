import sys
n,m=map(int, sys.stdin.readline().rstrip().split())
trees=list(map(int,sys.stdin.readline().rstrip().split()))
trees.sort(reverse=True)
hight=trees[0]

while True:
    hight-=1
    sum_tree=0
    for t in trees:
        if t>hight:
            sum_tree+=t-hight
    if sum_tree>=m:
        break

print(hight)
    

