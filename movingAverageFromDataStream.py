class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.sums = [0] * size
        self.count = 0
        self.size = size
    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        self.count += 1
        index = self.count % self.size
        preIndex = (self.count - 1) % self.size
        
        oldSum = self.sums[index]
        newSum = self.sums[preIndex] + val
        self.sums[index] = newSum
        if self.count <= self.size:
            return (newSum - oldSum) / self.count
        else:
            return (newSum - oldSum) / self.size
        
