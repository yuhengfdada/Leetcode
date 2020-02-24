#3711解法
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Value = {}
        Sum = {}
        Value[0] = nums[0]
        Maxvalue = nums[0]
        Minsum = min(0,nums[0])
        Sum[0] = nums[0]
        for i in range(1,len(nums)):
            Sum[i] = Sum[i-1] + nums[i]
            Value[i] = Sum[i] - Minsum
            if Value[i] > Maxvalue:
                Maxvalue = Value[i]
            if Sum[i] < Minsum:
                Minsum = Sum[i]
        return Maxvalue

原理是：从头到j的sum - 从头到i的sum（该sum最小）= 以j结尾的最大子数组。

#精简版
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums)):
            nums[i] += max(0,nums[i-1])
        return max(nums)
利用了正负性。
