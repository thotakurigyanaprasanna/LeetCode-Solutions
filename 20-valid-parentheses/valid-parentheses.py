class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=[]
        balanced=True
        for i in s:
            if i in "({[":
                l.append(i)
            elif i ==')' and l and l[-1]=='(':
                l.pop()
            elif i ==']' and l and l[-1]=='[':
                l.pop()
            elif i=='}' and l and l[-1]=='{':
                l.pop()
            else:
                balanced=False
        if l:
            return False
        return balanced
