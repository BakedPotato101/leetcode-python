class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummyHead = ListNode(0)
            currentNode = dummyHead
            carry = 0
            while l1 or l2:

                x = l1.val if l1 else 0
                y = l2.val if l2 else 0

                sum = x + y + carry

                carry = sum // 10

                currentNode.next = ListNode(sum % 10)
                currentNode = currentNode.next

                if l1:
                    l1 = l1.next

                if l2:
                    l2 = l2.next
                    
            if carry > 0:
                currentNode.next = ListNode(carry)
            return dummyHead.next