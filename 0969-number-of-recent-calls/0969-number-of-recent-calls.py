class RecentCounter(object):

    def __init__(self):
        self.RecentCounter = collections.deque()        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.RecentCounter.append(t)
        while(self.RecentCounter[0]<t-3000):
            self.RecentCounter.popleft()
        return len(self.RecentCounter)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)