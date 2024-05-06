class Solution:
    def removeNodes(self, n: Optional[ListNode]) -> Optional[ListNode]:
        return n.next and (setattr(n,'next',q:=self.removeNodes(n.next)),q)[n.val<q.val] or n
