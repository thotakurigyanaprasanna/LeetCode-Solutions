class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''.join(str(i) for i in digits)
        print(s)
        s1=int(s)
        s1=s1+1
        print(s1)
        return list(map(int,str(s1)))