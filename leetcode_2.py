class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def get_next(self):
        yield self.next
        yield from self.next.get_next()

    def get_last_item(self, item):
        if item.next:
            return self.get_last_item(item.next)
        else:
            return item
    def append_item(self, item):
        self.get_last_item(self).next = item

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        lr = ListNode(0)
        while l1.next or l2.next:




