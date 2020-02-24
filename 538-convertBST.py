#注意BST的结构，先遍历大的再遍历小的。
class Solution(object):
    larger_sum = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            self.convertBST(root.right)
            temp = root.val
            root.val += self.larger_sum
            self.larger_sum += temp
            self.convertBST(root.left)
            return root
        else:
            return None
