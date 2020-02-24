#Naive implementation: worst case O(n^2),best case O(n+1)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        support = {}
        for i in range(len(nums)):
            if nums[i] in support:
                support[nums[i]] += 1
            else:
                support[nums[i]] = 1
        for i in support:
            if support[i] > len(nums)/2:
                return i

#容易想到的优化: All cases O(n)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        support = {}
        for i in range(len(nums)):
            if nums[i] in support:
                support[nums[i]] += 1
            else:
                support[nums[i]] = 1
            if support[nums[i]] > len(nums)/2:
                return nums[i]

#已知最好方法（很难想到）
#摩尔投票法的基本思想很简单,在每一轮投票过程中,从数组中找出一对不同的元素,将其从数组中删除。这样不断的删除直到无法再进行投票
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = nums[0]
        count = 0
        for num in nums:
            if ret != num:
                count -= 1
                if count == 0:
                    ret = num 
                    count += 1
            else:
                count += 1
        return ret
