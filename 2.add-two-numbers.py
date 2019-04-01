# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def toInt(self, l: ListNode) -> int:
        return l.val + 10 * self.toInt(l.next) if l else 0

    def toListNode(self, n: int) -> ListNode:
        l = ListNode(n % 10)
        if n >= 10:
            l.next = self.toListNode(n // 10)
        return l

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.toListNode(self.toInt(l1) + self.toInt(l2))
