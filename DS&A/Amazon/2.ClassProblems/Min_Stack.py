class MinStack:
    def __init__(self):
        self.stack=[]
        self.minim= float("inf")

    def push(self, val: int) -> None:
        self.minim=min(self.minim,val)
        self.stack.insert(0,val)

    def pop(self) -> None:
        if self.minim == self.stack.pop(0):
            if self.stack:
                self.minim = min(self.stack)
            else:
                self.minim = float("inf")

    def top(self) -> int:
         return self.stack[0]

    def getMin(self) -> int:
        if self.stack:
            return self.minim
        else:
            return None
