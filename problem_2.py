class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_over = 0
        node = ListNode()
        home = ListNode(next=node)
        while l1 or l2:
            value_one = l1.val if l1 else 0
            value_two = l2.val if l2 else 0
            node.val = value_one + value_two + carry_over
            carry_over = node.val // 10
            node.val = node.val % 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if l1 or l2:
                node.next = ListNode()
                node = node.next
            elif carry_over != 0:
                node.next = ListNode(val=carry_over)

        return home.next
