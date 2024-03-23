class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        temp = head
        if count <= 2:
            return
        for i in range(count // 2):
            temp = temp.next
        prev = temp
        temp = temp.next
        for i in range(count - (count// 2) - 2):
            nex = temp.next
            temp.next = prev
            prev = temp
            temp = nex
        temp.next = prev
        p1 = head
        p2 = temp
        swap = 1
        for i in range(count - 1):
            if swap == 1:
                swap = 0
                nex = p1.next
                p1.next = p2
                p1 = nex
            elif swap == 0:
                swap = 1
                nex = p2.next
                p2.next = p1
                p2 = nex
        if swap == 0:
            p1.next = p2
            p2.next = None
        else:
            p2.next = p1
            p1.next = None
