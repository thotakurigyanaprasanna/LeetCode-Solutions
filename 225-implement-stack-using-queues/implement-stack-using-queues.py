class MyStack(object):

    def __init__(self):
        self.a=deque()
    def push(self, x):
        self.a.append(x)
        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        return self.a.pop()
        """
        :rtype: int
        """
        

    def top(self):
        """
        :rtype: int
        """
        return self.a[-1]


    def empty(self):
        """
        :rtype: bool
        """
        return len(self.a)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()