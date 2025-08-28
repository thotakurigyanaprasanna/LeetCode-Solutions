class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr=list(s.split())
        print(arr)
        l=0
        r=len(arr)-1
        while l<=r:
            arr[l]=arr[l][::-1]
            l+=1
        return " ".join(arr)