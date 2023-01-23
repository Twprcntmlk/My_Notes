#[5,2,2,2,2,6,3,4,7,5,6,1,8,9,10,11]


from collections import defaultdict

def contigNums(a): #[5,2,6,3,4,7,5,6,1,8,9]
  mp = defaultdict(lambda:0)
  n=len(a)
  # stores the length of the longest
  # subsequence that ends with a[i]
  dp = [0 for i in range(n)]
  maximum = 0

  # iterate for all element
  for i in range(n):

      # if a[i]-1 is present before i-th index
      if a[i] - 1 in mp:

          # last index of a[i]-1
          lastIndex = mp[a[i] - 1] - 1

          # relation
          dp[i] = 1 + dp[lastIndex]
      else:
          dp[i] = 1

          # stores the index as 1-index as we need to
          # check for occurrence, hence 0-th index
          # will not be possible to check
      mp[a[i]] = i + 1

      # stores the longest length
      maximum = max(maximum, dp[i])
  return maximum

print(contigNums([5,2,6,3,4,7,5,6,1,8,9]))
