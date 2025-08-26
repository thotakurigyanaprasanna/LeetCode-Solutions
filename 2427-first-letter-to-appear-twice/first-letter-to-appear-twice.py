class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        d={}
        for i in s:
            if i in d:
                return i
            else:
                d[i]=1