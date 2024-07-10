class Solution:
    def minOperations(self, logs: List[str]) -> int:
        st=[]
        for i in logs:
            if i=="./" or (i=="../" and not st):
                continue
            elif i=="../" and st:
                st.pop()
            else:
                st.append(i)
            print(st)
        return len(st)