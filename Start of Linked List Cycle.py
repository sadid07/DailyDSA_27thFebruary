# OG Solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def findIntersection(self, head):
        slow, fast = head, head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return slow

        return None

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        intersect = self.findIntersection(head)

        if intersect is None:
            return None

        p1 = head
        p2 = intersect

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next


        return p1






































"""
Good Attempt:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def calculate_cycle_length(slow):
            current = slow
            cycle_length = 0

            while True:
                current = current.next
                cycle_length += 1
                if current == slow:
                    break
            return cycle_length

        def find_start(head, cycle_length):
            pointer1 = head
            pointer2 = head

            while cycle_length > 0:
                pointer2 = pointer2.next
                cycle_length -= 1

            while pointer1 != pointer2:
                pointer1 = pointer1.next
                pointer2 = pointer2.next
            return pointer1


        def find_cycle_start(head):
            cycle_length = 0

            slow, fast = head, head
            while fast is not None and fast.next is not None:
                fast = fast.next.next
                slow = slow.next

                if slow == fast:
                    cycle_length = calculate_cycle_length(slow)
                    break
            return find_start(head, cycle_length)


"""