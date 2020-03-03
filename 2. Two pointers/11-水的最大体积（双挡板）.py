#我感觉可以这么理解：由于面积取决于边长短的那一端假设为m，所以要想得到比当前更大的面积，边长短的那一端必须舍弃，因为如果不舍弃，高最大就是m，而随着指针的移动宽会一直减小，因此面积只会越来越小。
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maximum = 0
        p1 = 0
        p2 = len(height) - 1
        while(p1!=p2):
            maximum = max(maximum,(p2-p1) * min(height[p1],height[p2]))
            if height[p1]<=height[p2]: p1 += 1
            else: p2 -= 1
        return maximum