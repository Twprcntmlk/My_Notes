#Time Complexity: O(Some Multiple Log(N))
#Space Complexity: O(1) #size of call stack

#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        def search(topRight,bottomLeft):
            #base case 1: if I go overbounds
            if topRight.x < bottomLeft.x or topRight.y < bottomLeft.y:
                return 0
            #base case 2: if I get down to a singular point and has ship
            elif topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
                if sea.hasShips(topRight,bottomLeft):
                    return 1
            #base case 3: if it is true when i get to bottom that there are no ships terminate
            if not sea.hasShips(topRight,bottomLeft):
                return 0
           ###################################################################
            midX=(bottomLeft.x+topRight.x)//2
            midY=(bottomLeft.y+topRight.y)//2
            midPoint=Point(midX, midY)
            ##############################################################
            topLeftQuad=search(Point(midPoint.x, topRight.y), Point(bottomLeft.x, midPoint.y+1))
            topRightQuad=search(topRight, Point(midPoint.x+1, midPoint.y+1))
            bottomLeftQuad=search(Point(topRight.x, midPoint.y), Point(midPoint.x+1,bottomLeft.y))
            bottomRightQuad=search(Point(midPoint.x, midPoint.y), bottomLeft)

            return topLeftQuad+topRightQuad+bottomLeftQuad+bottomRightQuad

        return search(topRight,bottomLeft)

#https://leetcode.com/problems/number-of-ships-in-a-rectangle/discuss/1024086/Divide-and-Conquer-or-Visual-%2B-Explanation-or-Python
