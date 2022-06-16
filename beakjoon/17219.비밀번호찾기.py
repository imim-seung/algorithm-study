import sys

n,m=map(int,sys.stdin.readline().rstrip().split())

pw_dic={}
for _ in range(n):
    site, pw=sys.stdin.readline().rstrip().split()
    pw_dic[site]=pw

for _ in range(m):
    print(pw_dic[sys.stdin.readline().rstrip()])