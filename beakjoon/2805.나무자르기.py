import sys

def cut_tree(trees, height):
    sum_t=0
    for t in trees:
        if t>height:
            sum_t+=t-height
    return sum_t

def binary_search(array,target,start, end):
    while start<=end:
        height=(start+end)//2
        tree_sum=cut_tree(array,height)
        if tree_sum==target:
            return height
        elif tree_sum<target:
            end=height-1
        else:
            start=height+1
            if start>end:
                return height
            
    return height-1


n,m=map(int, sys.stdin.readline().rstrip().split())
trees=list(map(int,sys.stdin.readline().rstrip().split()))
trees.sort(reverse=True)
print(binary_search(trees,m,0,trees[0]))

    

