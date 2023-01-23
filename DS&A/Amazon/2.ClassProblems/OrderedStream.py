class OrderedStream:
    def __init__(self, n: int):
        self.stream = [None]*n+1
        self.pointer = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        #### if after my pointer
        if self.pointer < idKey:
            return []
        ### increment to where the strem ends
        while self.pointer < len(self.stream) and self.stream[self.pointer] is not None:
            self.pointer += 1
        return self.stream[idKey:self.pointer]
