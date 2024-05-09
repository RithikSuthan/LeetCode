class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        j=0
        ans=0
        while(j<len(s)):
            if s[j] not in s[i:j]:
                j=j+1
            else:
                while(i<j and len(s)>j):
                    if s[i:j+1].count(s[j])<=1:
                        break
                    i=i+1
                j=j+1
            ans=max(ans,len(s[i:j]))
        return ans