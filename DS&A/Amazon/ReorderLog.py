
def reorderLogFiles(self, logs: List[str]) -> List[str]:

    letter_list = []
    digit_list = []

    for i in range(len(logs)):
        tokens = logs[i].split()
        if tokens[1].isalpha():
            letter_list.append(logs[i])
        else:
            digit_list.append(logs[i])

    letter_list = sorted(letter_list, key = lambda x:x.split()[0])
    letter_list = sorted(letter_list, key = lambda x:x.split()[1:])
    return letter_list + digit_list
