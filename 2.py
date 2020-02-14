#暴力，好蠢
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        flag1,flag2 = True, True
        first = l1.val + l2.val
        jin = first > 9
        if jin:
            first -= 10
        current1, current2 = l1, l2 
        last_node = ListNode(first)
        preserve = last_node
        while True:    
            if flag1 and flag2:
                current1, current2 = current1.next, current2.next  
            elif not flag1 and flag2:
                current2 = current2.next
            elif flag1 and not flag2:
                current1 = current1.next
                  
            if current1 != None and current2 != None:
                current_val = current1.val + current2.val
                if jin: 
                    current_val += 1
                jin = current_val > 9
                if jin:
                    current_val -= 10
                current_node = ListNode(current_val)
                last_node.next = current_node
                last_node = current_node
            elif current1 == None and current2 == None:
                if jin: 
                    current_val = 1
                    current_node = ListNode(current_val)
                    last_node.next = current_node
                break
            elif current1 == None:
                flag1 = False
                current_val = 0 + current2.val
                if jin: 
                    current_val += 1
                jin = current_val > 9
                if jin:
                    current_val -= 10
                current_node = ListNode(current_val)
                last_node.next = current_node
                last_node = current_node
            else: 
                flag2 = False
                current_val = current1.val + 0
                if jin: 
                    current_val += 1
                jin = current_val > 9
                if jin:
                    current_val -= 10
                current_node = ListNode(current_val)
                last_node.next = current_node
                last_node = current_node
        return preserve
        
心得：1.进位其实只要用整除和取余就行了（老毛病）
2.            if flag1 and flag2:
                current1, current2 = current1.next, current2.next  
            elif not flag1 and flag2:
                current2 = current2.next
            elif flag1 and not flag2:
                current1 = current1.next
           这段直接分开啊，两句的事。
           if current1!=None: current1 = current1.next
           if current2!=None: current2 = current1.next
3. 进一步就是 val1 = current1.val if current1 else 0
             val2 = current2.val if current2 else 0
             
#精简版
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        re = ListNode(0)
        r=re
        carry=0
        while(l1 or l2):
            x= l1.val if l1 else 0
            y= l2.val if l2 else 0
            s=carry+x+y
            carry=s//10
            r.next=ListNode(s%10)
            r=r.next
            if(l1!=None):l1=l1.next
            if(l2!=None):l2=l2.next
        if(carry>0):
            r.next=ListNode(1)
        return re.next
