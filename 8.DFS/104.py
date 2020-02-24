#easy，遍历一遍即可。但是空间复杂度最坏情况是O(N),average case是O(logN).
class Solution(object):
    maxCount = 0
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth(root,1)
        return self.maxCount
    
    def depth(self,root,count):
        if root:
            if count > self.maxCount: self.maxCount = count
            self.depth(root.left,count+1)
            self.depth(root.right,count+1)
