class Solution:
    def reverseParentheses(self, s: str) -> str:
        st=[]
        for i in s:
            if i!=")":
                st.append(i)
            if i==')':
                str1=[]
                while( st[-1]!="(" ):
                    str1.append(st.pop())
                if st[-1]=="(":
                    st.pop()
                while len(str1)!=0:
                    st.append(str1.pop(0))
        return "".join(st)