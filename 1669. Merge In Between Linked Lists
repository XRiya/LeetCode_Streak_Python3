class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp=list1
        l1=[]
        while temp:
            l1.append(temp.val)
            temp=temp.next
        temp=list2
        l2=[]
        while temp:
            l2.append(temp.val)
            temp=temp.next
        r=l1[:a:]
        for i in l2:
            r.append(i)
        r+=l1[b+1::]
        temp=head=ListNode(r[0])
        for i in r[1:]:
            head.next=ListNode(i)
            head=head.next
        return temp
