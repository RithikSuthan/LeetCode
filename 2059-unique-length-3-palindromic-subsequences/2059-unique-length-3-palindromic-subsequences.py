class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        st = set(s)
        for letter in st:
            l = s.index(letter)
            r= s.rindex(letter)
            lettersBetween = []
            if r-l+1 > 1:
                lettersBetween = set(s[l+1:r])
            ans += len(lettersBetween)
        return ans 