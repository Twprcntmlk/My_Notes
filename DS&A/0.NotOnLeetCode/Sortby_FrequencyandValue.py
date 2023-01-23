import collections
def solve(Input):
    count = collections.Counter(Input)
    return sorted(Input, key=lambda x: (count[x], x), reverse=True)

Input="fdjlfsdfsasadsfsghsgsdjsdgsdfg"
print(solve(Input))
