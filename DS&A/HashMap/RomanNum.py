def romanToInt(self, s: str) -> int:
    table = {'I': 1,'IV': 4,'V': 5,'IX': 9,'X': 10,'XL': 40,'L': 50,
            'XC': 90,'C': 100,'CD': 400,'D': 500,'CM': 900,'M': 1000}
    # I can uses table = zip(roman,numbers)

    if s in table:
        return table[s]
    toNum = 0
    i = 0
    while i < (len(s) - 1):
        if table[s[i+1]] <= table[s[i]]:
            toNum += table[s[i]]
            i += 1
        else:
            toNum += (table[s[i+1]] - table[s[i]])
            i += 2

    if i == len(s) - 1:
        toNum += table[s[i]]

    return toNum
