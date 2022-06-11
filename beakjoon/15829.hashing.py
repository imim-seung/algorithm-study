import sys 

length=int(sys.stdin.readline().rstrip())

word=list(sys.stdin.readline().rstrip())
hash=0
for index,w in enumerate(word):
  hash+=(ord(w)-96)*(31**index)

print(hash if hash < 1234567891 else hash%1234567891)
