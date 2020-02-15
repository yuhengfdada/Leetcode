#一开始想着反向推，结果不对。我佛了。
#O(n^2)的解法（tm超时了）
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        preserved = headB
        while(headA):
            headB = preserved
            while(headB):
                if headA == headB:
                    return headA
                headB = headB.next
            headA = headA.next
        return None
       
