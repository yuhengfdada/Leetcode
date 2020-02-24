#一开始想着反向推，结果不对。我佛了。
#O(mn)的解法（tm超时了）
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
#O(m+n)的解法
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        currentA = headA
        currentB = headB
        hashmap = {}
        while currentA:
            hashmap[id(currentA)] = currentA
            currentA = currentA.next
        while currentB:
            if id(currentB) in hashmap:
                return hashmap[id(currentB)]
            currentB = currentB.next
        return None
#O(min(m,n))的艺术解法
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB
        if not pA or not pB: return None
        while pA != pB:
            if not pA: pA = headB
            else: pA = pA.next
            if not pB: pB = headA
            else: pB = pB.next
        return pA
