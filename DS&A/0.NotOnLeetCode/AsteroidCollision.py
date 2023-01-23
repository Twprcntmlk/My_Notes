def asteroidCollision(direction, strength):
  asteroids=zip(direction,strength)
  stack=[]
  for idx, info in enumerate(asteroids):
    direc, stren = info
    if direc==1:
      stack.append([idx,direc,stren])
    else:
      while stack and stack[-1][1]>1 and stack[-1][2]<stren:
        stack.pop()
      if not stack or stack[-1][1]<1:
        stack.append([idx,direc,stren])
      elif stack[-1][2]==stren:
        stack.pop()
  return [x[0] for x in stack]

direction= [-1,1,-1]
strength=[5,2,1]
print(asteroidCollision(direction, strength))
