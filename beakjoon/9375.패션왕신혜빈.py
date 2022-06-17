from collections import defaultdict
import sys

test_case=int(sys.stdin.readline().rstrip())

for _ in range(test_case):
  clothes=defaultdict(list)
  
  for _ in range(int(sys.stdin.readline().rstrip())):
    c, category=sys.stdin.readline().rstrip().split()
    clothes[category].append(c)
  
  count=1
  for v in clothes.values():
    count*=(len(v)+1)
        
  print(count-1)




    

