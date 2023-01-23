# Time Complexity: O(N*M) 
# Space Complexity:O(1) #same but modified baord
def candyCrush(board):
    if not board:
        board

    done = True
    ## Crush Rows
    for row in range(len(board)):
        ## because I will be grabbing 3
        for col in range(len(board[0])-2):
            nums1=abs(board[row][col])
            nums2=abs(board[row][col+1])
            nums3=abs(board[row][col+2])

            if nums1 == nums2 == nums3 and nums1 !=0:
                board[row][col] = -nums1
                board[row][col+1] = -nums2
                board[row][col+2] = -nums3
                done =False

    ## Crush Cols
    for col in range(len(board[0])):
        ## because I will be grabbing 3
        for row in range(len(board)-2):
            nums1=abs(board[row][col])
            nums2=abs(board[row+1][col])
            nums3=abs(board[row+2][col])

            if nums1 == nums2 == nums3 and nums1 !=0:
                board[row][col] = -nums1
                board[row+1][col] = -nums2
                board[row+2][col] = -nums3
                done =False
    ##Gravity Like moving array to end problem
    if not done:
        for col in range(len(board[0])):
            ## because I will be grabbing 3
            idx=len(board)-1
            for row in range(len(board)-1,-1,-1):
                if board[row][col] > 0:
                    board[idx][col] = board[row][col]
                    idx-=1
            ##put zeros in missing pieces
            for row in range(idx,-1,-1):
                board[row][col]=0

    return board if done else candyCrush(board)


board =[[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]


print(candyCrush(board))
