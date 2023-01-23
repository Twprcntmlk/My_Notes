from collections import defaultdict

def FunWithAnagrams(text):
  table=defaultdict(list)
  result=[]
  for idx, string in enumerate(text):
    key = "".join(sorted(string))
    table[key].append(idx)

  for k,v in table.items():
    result.append(v[0])
  return result




text=["code","doce","ecod","framer","frame"]
print(FunWithAnagrams(text))
