class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        th=head
        while th:
            c=c+1
            th=th.next
        n=c//2
        th=head
        for i in range(n):
            th=th.next
        return th
