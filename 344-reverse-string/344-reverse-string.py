class Solution:
    def reverseString(self, s: List[str]) -> None:
        start, end = 0, len(s)-1
        while start<end:
            s[start],s[end]=s[end],s[start]
            start+=1
            end-=1
            
        """
        Do not return anything, modify s in-place instead.
        """
        