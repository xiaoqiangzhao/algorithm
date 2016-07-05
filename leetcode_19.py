class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        res = ListNode(0)
        res.next = head
        tmp = res
        for i in range(n):
            head = head.next
        while head != None:
            head = head.next
            tmp = tmp.next
        tmp.next = tmp.next.next
        return res.next

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    test = Solution()
    re = test.removeNthFromEnd(a, 2)
    print(a.val)
    print(a.next.val)
    print(a.next.next.val)
    print(a.next.next.next.val)
    print(a.next.next.next.next.val)

    # if re:
        # print(re.val)
        # while re.next != None:
            # print (re.next.val)


