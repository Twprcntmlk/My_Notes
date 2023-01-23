def GasBoard(board,gas):

    def dfs(row,col,gas):
        #base cases
        if gas == 0:
          return False
        if board[row][col] =="o":
          return True
        if board[row][col]=="g":
          gas+=5
        if board[row][col]==".":
          gas-=1
        board[row][col]="X"

        # iteration
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        for dx, dy in directions:
            if 0 <= row+dx < len(board) and 0 <= col+dy < len(board[0]) and board[row+dx][col+dy]!="X" and gas>0:
                if dfs(row+dx,col+dy,gas):
                    return True
        return False

##########################################################
    for row in range(len(board)):# dfs find A ==> dfs() ===> false
        for col in range(len(board[0])):
            if board[row][col] == "c":
                if dfs(row,col,gas):
                    return True
    return False
