
from collections import deque
import sys

n=int(sys.stdin.readline().rstrip())

cards=deque([i for i in range(1,n+1)])

while len(cards)>1:
  cards.popleft()
  if len(cards)==1:
    break
  cards.append(cards.popleft())

print(cards[0])

