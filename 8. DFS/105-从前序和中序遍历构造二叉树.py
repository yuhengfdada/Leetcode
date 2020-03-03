#自己写的，问题：太长。不会用内置函数和return值。
class Solution(object):
    newNode = []
    root = None
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.newNode = []
        self.root = None
        self.recursion(preorder,inorder,None,0,1)
        return self.root
    
    def recursion(self,preorder,subtree,pred,isLeft,isStart):
        if preorder==[] or subtree==[]: return None
        for j in range(len(preorder)):
            c = 0
            for i in range(len(subtree)):
                if preorder[j]==subtree[i]:
                    self.newNode.append(TreeNode(subtree[i]))
                    if isStart==1: self.root = self.newNode[-1]
                    elif isLeft==1: pred.left = self.newNode[-1]
                    else: pred.right = self.newNode[-1]
                    self.recursion(preorder[j:],subtree[:i],self.newNode[-1],1,0)
                    self.recursion(preorder[j:],subtree[i+1:],self.newNode[-1],0,0)
                    c = 1 
                    break 
            if c==1: break

#用index函数取代两层循环，用return值直接取代全局变量。
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        # 前序遍历第一个值为根节点
        root = TreeNode(preorder[0])
        # 因为没有重复元素，所以可以直接根据值来查找根节点在中序遍历中的位置
        mid = inorder.index(preorder[0])
        # 构建左子树
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # 构建右子树
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root
