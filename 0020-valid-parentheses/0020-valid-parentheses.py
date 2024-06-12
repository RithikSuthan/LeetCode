class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            if i in "({[":
                st.append(i)
            elif i in ")}]" and st:
                if i==")" and st[-1]=="(":
                    st.pop()
                elif i=="}" and st[-1]=="{":
                    st.pop()
                elif i=="]" and st[-1]=="[":
                    st.pop()
                else:
                    return False
            else:
                return False
        if(len(st)==0):
            return True
        return False
