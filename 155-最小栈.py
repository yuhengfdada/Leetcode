#常规做法（没考虑栈空的情况，其实不够严谨）
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = []
        self.Minarray = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.array.append(x)
        if len(self.Minarray) == 0 or x < self.Minarray[-1]:
            self.Minarray.append(x)
        else:
            self.Minarray.append(self.Minarray[-1])
        

    def pop(self):
        """
        :rtype: None
        """
        self.array.pop()
        self.Minarray.pop()

        

    def top(self):
        """
        :rtype: int
        """
        return self.array[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.Minarray[-1]
        
#Comments:其实还有一点优化空间，就是主栈push的大于最小值时辅助栈不push，主栈pop的是最小值时辅助栈才pop。
