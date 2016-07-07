class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def get_next(self):
        yield self.next
        yield from self.next.get_next()


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        res = ListNode(0)
        cac = 0
        up = 0
        tmp = res
        while l1 or l2:
            if l1 and l2:
                cac = l1.val + l2.val + up
                up = cac // 10
                left = cac % 10
                l1 = l1.next
                l2 = l2.next
            elif l1:
                cac = l1.val + up
                up = cac // 10
                left = cac %10
                l1 = l1.next
            else:
                cac = l2.val + up
                up = cac // 10
                left = cac %10
                l2 = l2.next
            tmp2 = ListNode(left)
            tmp.next = tmp2
            tmp = tmp.next
        if up == 1:
            tmp2 = ListNode(1)
            tmp.next = tmp2
        return res.next


if __name__ == "__main__":
    l1_1 = ListNode(0)
    # l1_2 = ListNode(4)
    # l1_3 = ListNode(3)
    # l1_1.next = l1_2
    # l1_2.next = l1_3

    l2_1 = ListNode(7)
    l2_2 = ListNode(3)
    # l2_3 = ListNode(7)
    l2_1.next = l2_2
    # l2_2.next = l2_3

    test = Solution()
    res = test.addTwoNumbers(l1_1, l2_1)

    while res !=None:
        print(res.val)
        res = res.next





