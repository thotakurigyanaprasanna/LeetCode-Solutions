class Solution:
    def isPalindrome(self, x: int) -> bool:
        r=str(x)
        if r[0]=='-':
            return False
        re=r[::-1]
        if r==re:
            return True
        return False