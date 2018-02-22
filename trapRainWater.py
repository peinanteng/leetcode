class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = []
        leftVal = 0
        for i in range(len(height)):
            leftVal = max(leftVal, height[i])
            left.append(leftVal)
        
        left.reverse()
        
        newheight = height[:]
        newheight.reverse()
        
        water = 0
        rightVal = 0
        for i in range(len(newheight)):
            rightVal = max(rightVal, newheight[i])
            water += min(rightVal, left[i]) - newheight[i]
        return water
        
