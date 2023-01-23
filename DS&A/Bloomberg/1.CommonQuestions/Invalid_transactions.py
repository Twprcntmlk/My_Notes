#Time Complexity - 0(N) # Space Complexity - O(N)
from collections import defaultdict
def invalidTransactions(transactions):
    if not transactions:
        return []
    seen = defaultdict(list) #{'alice': [(20, 800, 'mtv', 0), (50, 100, 'mtv', 1)]}
    invalid = set()

    for idx, transaction in enumerate(transactions):
        info = transaction.split(",")
        name = info[0]
        time = int(info[1])
        money = int(info[2])
        city = info[3]

        if money > 1000:
            invalid.add((transaction,idx))
        #build dict to store last transaction
        for prev_time, prev_city, previdx, prev_trans in seen[name]:
            #if I fail the parameters
            if abs(time - prev_time) <= 60 and city != prev_city:
                invalid.add((prev_trans,previdx))
                invalid.add((transaction,idx))

        #attention I'm going idx for unique and transaction to hold my prev
        # and use time, city to compare
        seen[name].append((time, city, idx, transaction))


    return  [x[0] for x in invalid] # turn back into list from set

print(invalidTransactions(["alice,20,800,mtv","alice,50,600,jina","bob,50,1200,mtv"]))
