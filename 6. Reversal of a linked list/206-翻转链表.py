#递归
class Solution(object):
    before = None
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if head.next:
            hehe = head.next
            head.next = self.before
            self.before = head
            return self.reverseList(hehe)
        else:
            head.next = self.before
            return head
