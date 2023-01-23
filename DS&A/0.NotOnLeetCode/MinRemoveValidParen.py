def minRemoveToMakeValid(self, s: str) -> str:

    # Pass 1: Remove all invalid ")"
    first_pass_chars = []
    balance = 0
    open_seen = 0
    for char in s:
        if char == "(":
            balance += 1
            open_seen += 1
        if char == ")":
            if balance == 0:
                continue # skip all the ")"
            balance -= 1
        first_pass_chars.append(char)

    print(first_pass_chars)

    # Pass 2: Remove the rightmost "("
    result = []
    open_to_keep = open_seen - balance
    # this way I keep the front "(" and then remove then after
    for char in first_pass_chars:
        if char == "(":
            open_to_keep -= 1
            if open_to_keep < 0: #skip all "("
                continue
        result.append(char)

    return "".join(result)
