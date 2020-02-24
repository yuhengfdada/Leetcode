#经典动态规划
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = {}
        a[1] = 1
        a[2] = 2
        for i in range(3,n+1):
            a[i] = a[i-2] + a[i-1]
        return a[n]
