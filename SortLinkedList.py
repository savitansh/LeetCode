class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        p = head.next
        while p is not None:
            old = p.next
            if p.val!=head.val:
                head = self.removeNode(p, head)
                head = self.insertNodeMaintainingOrder(p, head)
            p = old
        return head

    def removeNode(self, p, head):
        tmp = head
        while tmp.next != p:
            tmp = tmp.next
        if tmp.next == p:
            tmp.next = p.next
        return head

    def insertNodeMaintainingOrder(self, p, head):
        if head.val > p.val:
            p.next = head
            tmp = head
            head = p
            return head
        tmp = head
        t2 = tmp.next
        while t2 is not None and t2 != p and t2.val <= p.val:
            tmp = t2
            t2 = t2.next
        if t2 is None or t2.val > p.val:
            tmp.next = p
            p.next = t2
        else:
            t3 = t2.next
            p.next = t3
            t2.next = p
        return head


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    p1 = ListNode(1)
    p2 = ListNode(1)
    head.next = p1
    p1.next = p2
    # p2.next = p3
    # p3.next = p4
    head = s.sortList(head)
    while head is not None:
        print(head.val)
        head = head.next
