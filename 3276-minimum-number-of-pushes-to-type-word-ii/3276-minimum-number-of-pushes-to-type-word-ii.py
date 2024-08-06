class Solution:
    from collections import defaultdict
    def minimumPushes(self, word: str) -> int:
        dict1=defaultdict()
        pad=defaultdict()
        for i in range(2,10):
            pad[i]=[]
        for i in set(word):
            dict1[i]=word.count(i)
        dict1=dict(sorted(dict1.items(), key=lambda x:x[1],reverse=True))
        # print(dict1)
        iter=2
        for i in dict1:
            pad[iter].append(i)
            iter+=1
            if iter==10:
                iter=2
        # print(pad)
        min_ans=0 
        for i in word:
            for ele in pad:
                if i in pad[ele]:
                    min_ans+=pad[ele].index(i)+1
                    break
        return min_ans