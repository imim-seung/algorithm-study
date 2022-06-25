from collections import defaultdict
import sys

n=int(sys.stdin.readline().rstrip())

book_dic=defaultdict(int)
for _ in range(n):
  book_dic[sys.stdin.readline().rstrip()]+=1

max_count=max(book_dic.values())
best_seller=[]
for n in book_dic:
  if book_dic[n]==max_count:
    best_seller.append(n)

best_seller.sort()
print(best_seller[0])
