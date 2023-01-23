#Time: O(n) Space:O(n)
def kthFactor(n, k):
    factors=[] #[1, 2, 3, 4, 6, 9, 12, 18, 36]
    for i in range(1, n+1):
        if n%i==0:
            factors.append(i)
    if factors[k-1]:
        return factors[k-1]
    else:
        return -1

print(kthFactor(36, 4))
