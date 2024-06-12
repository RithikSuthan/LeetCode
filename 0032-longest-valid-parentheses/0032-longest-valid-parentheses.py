class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_val=0
        st=[-1]
        for i in range(len(s)):
            if s[i] == "(":
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                max_val=max(max_val,i-st[-1])
        if max_val!=0:
            return max_val 
        return 0