def FibMemo(n, memo ={0:0,1:1,2:1}):
  if n in memo:
    return memo[n]
  else:
    memo[n] = FibMemo(n-1,memo) + FibMemo(n-2,memo)
  return memo[n]


def FibTab(n):
  i=0
  tab = [0]*(n+5)

  tab[1]=1
  while i <= n:
    tab[i+1]+=tab[i]
    tab[i+2]+=tab[i]
    i+=1

  return tab[n]




print(FibMemo(4))
1,1,2,3,5,8,13,21

print(FibTab(4))
1,1,2,3,5,8,13,21
