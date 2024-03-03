class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        result = []

        while current:
            result.append(current.val)
            current = current.next

        result = result[:-n] + (result[-n+1:] if n > 1 else [])

        next = None
        i = len(result) - 1

        while i >= 0:
            current = ListNode(result[i], next)
            next = current
            i -= 1

        return current
