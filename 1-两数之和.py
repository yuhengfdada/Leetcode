#一开始的solution，两层循环
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j] == target and i != j:
                    return [i,j]
                    
#Hashmap
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap={}
        for index,num in enumerate(nums):
            another = target - num
            if another in hashmap:
                return[hashmap[another],index]
            hashmap[num] = index
其实这个也不太算真的hashmap，因为相同的数会被覆盖（key的唯一性）。然而因为只是“两数之和”所以没事。
