import Queue
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = Queue.Queue()
        self.queue2 = Queue.Queue()
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue1.put(x)
        
            

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())
        item = self.queue1.get()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return item
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())
        item = self.queue1.get()
        self.queue2.put(item)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return item

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.queue1.qsize() == 0
