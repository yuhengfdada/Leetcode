#从叶到根递归
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            self.invertTree(root.left)
            self.invertTree(root.right)
            temp = root.right
            root.right = root.left
            root.left = temp
        return root
