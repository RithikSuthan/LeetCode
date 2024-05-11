class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dict1={}
        ans=[]
        for i in range(len(points)):
            if ((points[i][0]**2)+(points[i][1]**2))**0.5 in dict1:
                dict1[ ((points[i][0]**2)+(points[i][1]**2))**0.5 ].append(i)
            else:
                dict1[ ((points[i][0]**2)+(points[i][1]**2))**0.5 ]=[i]
        dict2=sorted(dict1.keys())
        # print(dict1)
        for i in range(k):
            if i<len(dict2):
                for j in dict1[dict2[i]]:
                    if len(ans)<k:
                        ans.append(points[j])
        # print(ans)
        return ans