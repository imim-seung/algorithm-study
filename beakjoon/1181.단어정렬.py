#1. 길이가 짧은 것 부터 
#2. 길이가 같으면 사전순으로 

n=int(input())
words=[]
for _ in range(n):
  words.append(input())
words=list(set(words))
words.sort(key=lambda x : (len(x),x))

for w in words:
  print(w)
