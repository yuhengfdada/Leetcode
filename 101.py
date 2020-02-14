#递归点在“左的左等于右的右，左的右等于右的左”
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        return self.isMirror(root.left,root.right)

    def isMirror(self,left,right):
        if left==None and right==None : 
            return True 
        elif left==None or right==None or left.val!=right.val: 
            return False
        else:
            return self.isMirror(left.left,right.right) and self.isMirror(left.right,right.left)
#迭代（知识点：层序遍历）
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root]
        while(queue): #while(queue不是全空)
            next_queue = []
            layer = []
            for node in queue:
                if not node:
                    layer.append(None)
                else:
                    next_queue.append(node.left)
                    next_queue.append(node.right)
                    layer.append(node.val)
            if layer[::-1]!=layer:
                return False
            queue = next_queue
        return True
