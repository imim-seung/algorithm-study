from collections import defaultdict

def solution(s1, s2, k):
    answer = []
    subjects=defaultdict(list)
    
    for a,b in zip(s1,s2):
      subjects[b].append(a)
      
    for key in subjects:
      subjects[key].sort()

    stack=[k]

    while stack:
      s=stack[-1]
      if subjects[s]:
        stack.extend(subjects[s])
        subjects[s]=[]
      else : 
        answer.append(stack.pop())
        




    return answer