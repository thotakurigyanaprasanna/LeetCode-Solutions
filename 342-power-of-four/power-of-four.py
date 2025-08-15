class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        if n<=0:
            return False
        b=bin(n)[2:]
        print(b)
        if b.count('0')%2==0 and b.count('1')==1:
            return True
        return False