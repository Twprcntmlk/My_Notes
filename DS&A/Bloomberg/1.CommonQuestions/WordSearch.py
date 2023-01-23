#Time Complexity: O(N*3^L) (3^L == number of traversals and the length of the word)
#Space Complexity: O(n)
def exist(board, word):
    def dfs(row,col,newword):
        #base cases
        if len(newword)==0:
            return True
        #mark
        temp = board[row][col]
        board[row][col]="0"
        # iteration
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        for dx, dy in directions:
            if 0 <= row+dx < len(board) and 0 <= col+dy < len(board[0]) and board[row+dx][col+dy]== newword[0]:
                if dfs(row+dx,col+dy,newword[1:]):
                    return True
        board[row][col]= temp
        return False
##########################################################
    for row in range(len(board)):# dfs find A ==> dfs() ===> false
        for col in range(len(board[0])):
            if board[row][col] == word[0]:
                if dfs(row,col,word[1:]):
                    return True
    return False
