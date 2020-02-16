#我吐了兄弟们。
#第一个想法是：先遍历一遍找到所有叶子，然后反推所有从头到尾的路径，再看子数组之和等于sum的个数。
#结果写到最后发现叶子不同但中间有sum就会算两次。我佛。
class Solution(object):
    def pathSum(self, root, sum1):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.pred = {}
        self.leaves = []
        count = 0
        self.bianli(root,None)
        print(self.leaves)
        for leaf in self.leaves:
            leaf_update = leaf
            array = []
            while leaf_update:
                array.append(leaf_update.val)
                leaf_update = self.pred[leaf_update]
            print(array)
            for i in range(len(array)):
                for j in range(len(array)):
                    if sum(array[i:j]) == sum1:
                        count += 1
                        print(i,j)
        return count
    def bianli(self,root,pre):
        if not root:
            return False
        else:
            self.pred[root] = pre
            b1 = self.bianli(root.left,root)
            b2 = self.bianli(root.right,root)
            if not b1 and not b2:
                self.leaves.append(root)
            return True
            
#递归写法。还是要遍历，但是关键在于：在遍历的时候就要同时寻找子数组。
#懒得写了，抄个别人写的java O(nlogn)
 public int pathSum(TreeNode root, int sum) {
        return pathSum(root, sum, new int[1000], 0);
    }

    public int pathSum(TreeNode root, int sum, int[] array/*保存路径*/, int p/*指向路径终点*/) {
        if (root == null) {
            return 0;
        }
        int tmp = root.val;
        int n = root.val == sum ? 1 : 0;
        for (int i = p - 1; i >= 0; i--) {
            tmp += array[i];
            if (tmp == sum) {
                n++;
            }
        }
        array[p] = root.val;
        int n1 = pathSum(root.left, sum, array, p + 1);
        int n2 = pathSum(root.right, sum, array, p + 1);
        return n + n1 + n2;
    }
#联动560：和为k的子数组。
#思想：令sum[i]等于i及之前所有元素的和。如果[i+1,j]的和为k，那么sum[j]-sum[i]=k。所以要找到以j结尾的和为k的子数组，
#只要查找之前出现过几次sum[i]=sum[j]-k就行了。
#Hashmap储存{sum:该sum出现的次数}
#利用这个可以优化上面那个到O(n)?
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        Hashmap = {0:1}
        Sum = 0
        count = 0
        for i in range(len(nums)):
            Sum += nums[i]
            if Sum in Hashmap:
                Hashmap[Sum] += 1
            else:
                Hashmap[Sum] = 1
            if (Sum - k) in Hashmap:
                count += Hashmap[Sum-k]
                if k == 0:
                    count -= 1
        return count





