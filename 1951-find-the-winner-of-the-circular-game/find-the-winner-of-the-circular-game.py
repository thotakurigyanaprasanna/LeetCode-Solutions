class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        l=list(range(1,n+1))
        i=0
        while len(l)>1:
            i=(i+k-1)%len(l)
            l.pop(i)
        return l[0]