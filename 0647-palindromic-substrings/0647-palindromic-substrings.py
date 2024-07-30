class Solution:
    def countSubstrings(self, s: str) -> int:
        ans=[]
        for i in range(0,len(s)):
            # print("Frame ",i)
            left=0
            right=i
            while(left<=right and right<len(s)):
                if s[left:right+1]==s[left:right+1][::-1]:
                    ans.append(s[left:right+1])
                # print(s[left:right+1])
                right+=1
                left+=1
        return len(ans)