#使用额外空间的做法很简单：再创建一个一样的数组，在对应位置做“标记”即可。
#不使用额外空间，只要想办法在本数组的对应位置做“标记”。这里用的是置负值，确实还不错。
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for i in range(len(nums)):
            nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])
        for i in range(len(nums)):
            if nums[i]>0:
                ret.append(i+1)
        return ret
