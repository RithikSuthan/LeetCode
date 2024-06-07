class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        st=[]
        ans=[0 for i in range(len(temperatures))]
        i=0
        while(i<len(temperatures)-1):
            st.append(i)
            while( st and temperatures[st[-1]]<temperatures[i+1]):
                ans[st[-1]]=i-st[-1]+1
                st.pop()
            i=i+1
        # print(ans)
        return ans

        