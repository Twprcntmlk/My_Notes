def solve(n):
    total = 0

    for coin in [25, 10, 5, 1]:
        this_coin = n // coin
        total += this_coin
        n -= coin * this_coin

        if n == 0:
            break

    return total
print(solve(100))
