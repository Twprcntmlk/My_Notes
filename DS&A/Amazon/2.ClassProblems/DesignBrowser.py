#Time Complexity: O()
#Space Complexity: O()
class DLLNode:
    def __init__(self, val=0, prev=None, next= None):
        self.val = val
        self.prev = prev
        self.next =next

class BrowserHistory:
    def __init__(self, homepage: str):
        self.home = DLLNode(homepage)
        self.moving = self.home

    def visit(self, url: str) -> None:
        self.moving.next = DLLNode(url)
        self.moving.next.prev = self.moving  ## move to next page
        self.moving = self.moving.next

    def back(self, steps: int) -> str:
        while steps and self.moving.prev:
            steps -=1
            self.moving = self.moving.prev
        return self.moving.val

    def forward(self, steps: int) -> str:
        while steps and self.moving.next:
            steps -=1 #MINUS!!!!!!!!!!!!!!!
            self.moving = self.moving.next
        return self.moving.val

#"What if you had a capacity, how would you approach?" -> Basically LRU cache
#If there are no URL's (i.e. dummyHead is pointing to dummyTail)
# is there any reason to do an if check so we just return an empty list?" -
# > yes I would still do an if check to tell user there is an error or exception?


# class BrowserHistory:
#     def __init__(self, homepage: str):
#         self.current=0
#         self.history=[homepage]

#     def visit(self, url: str) -> None:
#         self.current+=1
#         #increase browser length
#         self.history=self.history[:self.current]
#         self.history.append(url)

#     def back(self, steps: int) -> str:
#         #give me either the first thing or however many back
#         self.current=max(self.current-steps, 0)
#         return self.history[self.current]

#     def forward(self, steps: int) -> str:
#         #give me either the last thing or however many forwards
#         self.current=min(self.current+steps, len(self.history)-1)
#         return self.history[self.current]
