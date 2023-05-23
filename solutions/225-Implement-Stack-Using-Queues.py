class MyStack(object):

    # Constructor to create our deque
    def __init__(self):
        self.q = deque()

    # Push to end
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x)

    # Pop elements and pushing to the end
    def pop(self):
        """
        :rtype: int
        """
        # Push all but the last element to the end
        for i in range(len(self.q)-1):
            self.push(self.q.popleft())
        
        # return the popped element
        return self.q.popleft()

    # Peek at top of list
    def top(self):
        """
        :rtype: int
        """
        return self.q[-1]
        
    # Check if empty
    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()