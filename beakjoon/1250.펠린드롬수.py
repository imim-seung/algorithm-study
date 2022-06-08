from collections import deque
def is_palen(a):
  queue=deque(list(a))
  while len(queue)>1:
    a=queue.pop()
    b=queue.popleft()
    if a != b:
      return False
  return True

num=input()
while num !='0':
  print('yes' if is_palen(num) else 'no')
  num=input()

