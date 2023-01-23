# Interview started with basic introduction (talked about myself and the favorite project that I worked on),
# then went to the HackerRank link provided to work on a coding challenge

# The question:

# Interviewer drew out the illustration exactly as shown below
# <----- 0-----0--0----
# ----1-----1--------1->

# On a 2 ways lane, there are cars driving west-bound (0) and cars driving east-bound (1),
# write a function that returns the amount of times that the cars will pass by each other.

# The above illustration was turned into an array [1,0,1,0,0,1] as input and should return 5
# (first "1" will drive by 3 "0", second will drive by 2, and third will drive by 0).

def CarPass(arr):
    numberOfOnes=0
    passes=0
    for num in arr:
        if num == 1:
            numberOfOnes+=1
        else:
            passes+=numberOfOnes
    return passes

arr=[1,0,1,0,0,1]
print(CarPass(arr))

# concept
# [1,0,1,0,0,1]
# for the 1st Zero there was One 1 that passed
# for the 2nd and 3rd Zero Two 1 passed
# then there are no more zeros but any zero pass the 3rd one would add 3 per Zero
