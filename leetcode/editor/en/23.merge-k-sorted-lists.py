# Merge k sorted linked lists and return it as one sorted list. Analyze and descr
# ibe its complexity.
#
# Example: 
#
# 
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6
# 
# Related Topics Linked List Divide and Conquer Heap


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nums = []
        for node in lists:
            while node:
                nums.append(node.val)
                node = node.next
        nums.sort()
        if not nums:
            return None
        head = ListNode(nums[0])
        current = head
        for num in nums[1:]:
            current.next = ListNode(num)
            current = current.next
        return head

# leetcode submit region end(Prohibit modification and deletion)
