class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList(object):

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0 and curr != self.right:
            return curr.val
        return -1
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = ListNode(val)
        next = self.left.next
        prev = self.left

        prev.next = new_node
        next.prev = new_node

        new_node.prev = prev
        new_node.next = next
        
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = ListNode(val)
        next = self.right
        prev = self.right.prev

        prev.next = new_node
        next.prev = new_node

        new_node.prev = prev
        new_node.next = next
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index = index - 1
        if curr and index == 0:
            new_node = ListNode(val)
            next = curr
            prev = curr.prev

            prev.next = new_node
            next.prev = new_node
            new_node.prev = prev
            new_node.next = next

        

    def deleteAtIndex(self, index):
        node = self.left.next
        while node and index > 0:
            node = node.next
            index -= 1
        
        if node and node != self.right and index == 0:
            node.prev.next = node.next
            node.next.prev = node.prev
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)