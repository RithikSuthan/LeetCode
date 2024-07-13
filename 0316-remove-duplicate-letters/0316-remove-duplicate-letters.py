class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq={}
        for i in set(s):
            freq[i]=s.count(i)
        seen=set()
        st=[]
        for i in s:
            freq[i]-=1
            if i in seen:
                continue
            while st and freq[st[-1]]>0  and st[-1]>i:
                seen.remove(st.pop())
            st.append(i)
            seen.add(i)
        return "".join(st)