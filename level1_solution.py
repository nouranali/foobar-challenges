from __future__ import division
from __future__ import print_function

def solution(s):
    # Your code here
  if not bool(s):
    return 0
  res=0
  ln=len(s)
  i=ln
  while i>0:
    tmp=ln/i
    if (tmp*i == ln):
      valid=True
      st=s[:int(tmp)]
      j=1
      while j<i:
        if not s[int(j*tmp):int(j*tmp+tmp)] ==st:
          valid=False
          break
        j=j+1
    if bool(valid):
      res=i
      break
    i=i-1
  return res    


        
        


