from collections import defaultdict
import sys

n=sys.stdin.readline().rstrip()
cards_dic=defaultdict(int)
for num in list(map(int,sys.stdin.readline().rstrip().split())):
  cards_dic[num]+=1

m=sys.stdin.readline().rstrip()

for target in list(map(int,sys.stdin.readline().rstrip().split())):
  if target in cards_dic:
    print(cards_dic[target], end=' ')
  else: 
    print(0, end=' ')
  