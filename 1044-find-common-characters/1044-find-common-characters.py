class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        first=words[0]
        ans=[]
        for i in first:
            if i not in ans:
                val=first.count(i)
                for j in range(1,len(words)):
                    val=min(val,words[j].count(i))
                    if val==0:
                        break
                for k in range(val):
                    ans.append(i)
                # print(ans)
        return ans
            


        
