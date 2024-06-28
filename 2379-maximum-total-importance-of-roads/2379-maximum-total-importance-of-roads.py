class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        dict1={}
        dict2={}
        rank=[0 for i in range(n)]
        ans=0
        for road in roads:
            if road[0] not in dict1:
                dict1[road[0]]=[]
                dict2[road[0]]=0
            if road[1] not in dict1:
                dict1[road[1]]=[]
                dict2[road[1]]=0
            dict1[road[0]].append(road[1])
            dict1[road[1]].append(road[0])
                            
            dict2[road[0]]=len(dict1[road[0]])
            dict2[road[1]]=len(dict1[road[1]])
            
        print(dict1)
        print(dict2)

        sorted_dict2=dict(sorted(dict2.items(),key=lambda x:x[1],reverse=True))
        print(sorted_dict2)
        cou=n
        for i in sorted_dict2:
            rank[i]=n
            n-=1
        print(rank)

        for road in roads:
            ans+=rank[road[0]]+rank[road[1]]
        return ans                