# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def toStr(self, l: ListNode) -> str:
        if not l:
            return ""
        return str(l.val) + self.toStr(l.next)

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        values = sorted(list("".join(self.toStr(l) for l in lists)))
        root = ListNode(values[0] if values else None)
        cur = root
        for i in values[1:]:
            cur.next = ListNode(i)
            cur = cur.next
        return root
