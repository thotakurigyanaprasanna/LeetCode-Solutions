class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v=['a','e','i','o','u','A','E','I','O','U']
        arr=list(s)
        l=0
        r=len(arr)-1
        while l<r:
            if arr[l] in v and arr[r] in v:
                t=arr[l]
                arr[l]=arr[r]
                arr[r]=t
                l+=1
                r-=1
            elif arr[l] not in v:
                l+=1
            else:
                r-=1
        return ''.join(arr)